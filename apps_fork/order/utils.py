from oscar.apps.order.utils import OrderCreator as CoreOrderCreator

class OrderCreator(CoreOrderCreator):

    def place_order(self, basket, total,  # noqa (too complex (12))
                    shipping_method, shipping_charge, user=None,
                    shipping_address=None, billing_address=None,
                    order_number=None, status=None, request=None, **kwargs):
        """
        Placing an order involves creating all the relevant models based on the
        basket and session data.
        """
        if basket.is_empty:
            raise ValueError(_("Empty baskets cannot be submitted"))
        if not order_number:
            generator = OrderNumberGenerator()
            order_number = generator.order_number(basket)
        if not status and hasattr(settings, 'OSCAR_INITIAL_ORDER_STATUS'):
            status = getattr(settings, 'OSCAR_INITIAL_ORDER_STATUS')

        if Order._default_manager.filter(number=order_number).exists():
            raise ValueError(_("There is already an order with number %s")
                             % order_number)

        with transaction.atomic():

            # Ok - everything seems to be in order, let's place the order """""""""""""""""""""""""""TO UPDATE
            if basket.is_multi_partner:
                for partner_id in basket.partner_list:
                    temp_order_number = str(order_number) + "P" + str(partner_id)
                    order = self.create_order_model(
                        user, basket, shipping_address, shipping_method, shipping_charge,
                        billing_address, total, temp_order_number, status, request, **kwargs)
                    for line in basket.partner_lines(partner_id): ## all lines per partner_id
                        self.create_line_models(order, line)
                        self.update_stock_records(line)

            else:

                order = self.create_order_model(
                    user, basket, shipping_address, shipping_method, shipping_charge,
                    billing_address, total, order_number, status, request, **kwargs)
                for line in basket.all_lines():
                    self.create_line_models(order, line)
                    self.update_stock_records(line)

            for voucher in basket.vouchers.select_for_update():
                available_to_user, msg = voucher.is_available_to_user(user=user)
                if not voucher.is_active() or not available_to_user:
                    raise ValueError(msg)

            # Record any discounts associated with this order
            for application in basket.offer_applications:
                # Trigger any deferred benefits from offers and capture the
                # resulting message
                application['message'] \
                    = application['offer'].apply_deferred_benefit(basket, order,
                                                                  application)
                # Record offer application results
                if application['result'].affects_shipping:
                    # Skip zero shipping discounts
                    shipping_discount = shipping_method.discount(basket)
                    if shipping_discount <= D('0.00'):
                        continue
                    # If a shipping offer, we need to grab the actual discount off
                    # the shipping method instance, which should be wrapped in an
                    # OfferDiscount instance.
                    application['discount'] = shipping_discount
                self.create_discount_model(order, application)
                self.record_discount(application)

            for voucher in basket.vouchers.all():
                self.record_voucher_usage(order, voucher, user)

        # Send signal for analytics to pick up
        order_placed.send(sender=self, order=order, user=user)

        return order