from oscar.apps.shipping import methods
from oscar.core import prices
from decimal import Decimal as D
from decimal import *
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class MultiMethod(methods.FixedPrice):

    """ shipping method which can hold multi shipping methods, one fo each partner """

    name = _('Multi Method')
    exponent = D('0.00')
    sub_method = {}

    def __init__(self, selected_method, basket):
        rate = D(settings.OSCAR_DEFAULT_TAX_RATE)
        exponent = D('0.00')

        if basket.is_multi_partner:

            self.charge_incl_tax = 0
            self.charge_excl_tax = 0

            # add all shipping methods for every partner
            for partner in selected_method.keys():
                self.sub_method[partner] = MainMethod(selected_method[partner], basket)

                self.charge_incl_tax += self.sub_method[partner].calculate(basket).incl_tax
                self.charge_excl_tax += self.sub_method[partner].calculate(basket).excl_tax

            # do the global shipping setup
            if basket.total_incl_tax['parent'] > selected_method[basket.partner_list[0]].free_shipping_threshold:
                self.charge_incl_tax = D('0.00')
                self.charge_excl_tax = D('0.00')


        # if there is only one partner for the order
        else:
            if basket.total_incl_tax > selected_method[basket.partner_list[0]].free_shipping_threshold:
                self.charge_incl_tax = D('0.00')
                self.charge_excl_tax = D('0.00')
            else:
                self.charge_incl_tax = selected_method[basket.partner_list[0]].charge_incl_tax
                self.charge_excl_tax = self.charge_incl_tax/(1 + rate)


    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)

    @property
    def is_tax_known(self):
        return True


class MainMethod(methods.FixedPrice):

    """ simple methode includes within multi method """

    name = ''
    exponent = D('0.00')

    def __init__(self, method, basket):
        rate = D(settings.OSCAR_DEFAULT_TAX_RATE)
        exponent = D('0.00')
        self.name = method.name
        self.description = method.description

        # check if partner sub-total incl tax
        # is greater than threshold
        if basket.total_incl_tax[method.partner] > method.free_shipping_threshold:
            self.charge_incl_tax = D('0.00')
        else:
            self.charge_incl_tax = method.charge_incl_tax

        self.charge_excl_tax = self.charge_incl_tax/(1 + rate)

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax,
            incl_tax=self.charge_incl_tax)

    @property
    def is_tax_known(self):
        return True


class Free(methods.FixedPrice):
    """
    This shipping method specifies that shipping is free.
    """
    code = 'free-shipping'
    name = _('Free shipping')

    def calculate(self,basket):
        # If the charge is free then tax must be free (musn't it?) and so we
        # immediately set the tax to zero
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), tax=D('0.00'))
