# Generated by Django 2.2.13 on 2020-08-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_auto_20200806_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplacesettings',
            name='menu_url_1',
            field=models.URLField(blank=True, default='', null=True, verbose_name='URL 1'),
        ),
    ]
