# Generated by Django 2.2.13 on 2020-08-06 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20200805_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketplacesettings',
            name='product_tags',
        ),
    ]
