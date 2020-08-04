# Generated by Django 2.2.13 on 2020-08-04 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oscar.core.utils
import oscar.models.fields
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, db_index=True, max_length=128, verbose_name='Name')),
                ('users', models.ManyToManyField(blank=True, related_name='partners', to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'verbose_name': 'Fulfillment partner',
                'verbose_name_plural': 'Fulfillment partners',
                'ordering': ('name', 'code'),
                'permissions': (('dashboard_access', 'Can access dashboard'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StockRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_sku', models.CharField(max_length=128, verbose_name='Partner SKU')),
                ('price_currency', models.CharField(default=oscar.core.utils.get_default_currency, max_length=12, verbose_name='Currency')),
                ('price_excl_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Price (excl. tax)')),
                ('price_retail', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Price (retail)')),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Cost Price')),
                ('num_in_stock', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number in stock')),
                ('num_allocated', models.IntegerField(blank=True, null=True, verbose_name='Number allocated')),
                ('low_stock_threshold', models.PositiveIntegerField(blank=True, null=True, verbose_name='Low Stock Threshold')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockrecords', to='partner.Partner', verbose_name='Partner')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stockrecords', to='catalogue.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Stock record',
                'verbose_name_plural': 'Stock records',
                'abstract': False,
                'unique_together': {('partner', 'partner_sku')},
            },
        ),
        migrations.CreateModel(
            name='StockAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold', models.PositiveIntegerField(verbose_name='Threshold')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=128, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date Created')),
                ('date_closed', models.DateTimeField(blank=True, null=True, verbose_name='Date Closed')),
                ('stockrecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='partner.StockRecord', verbose_name='Stock Record')),
            ],
            options={
                'verbose_name': 'Stock alert',
                'verbose_name_plural': 'Stock alerts',
                'ordering': ('-date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')], max_length=64, verbose_name='Title')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last name')),
                ('line1', models.CharField(max_length=255, verbose_name='First line of address')),
                ('line2', models.CharField(blank=True, max_length=255, verbose_name='Second line of address')),
                ('line3', models.CharField(blank=True, max_length=255, verbose_name='Third line of address')),
                ('line4', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State/County')),
                ('postcode', oscar.models.fields.UppercaseCharField(blank=True, max_length=64, verbose_name='Post/Zip-code')),
                ('search_text', models.TextField(editable=False, verbose_name='Search text - used only for searching addresses')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Country', verbose_name='Country')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='partner.Partner', verbose_name='Partner')),
            ],
            options={
                'verbose_name': 'Partner address',
                'verbose_name_plural': 'Partner addresses',
                'abstract': False,
            },
        ),
    ]
