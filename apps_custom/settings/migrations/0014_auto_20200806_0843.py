# Generated by Django 2.2.13 on 2020-08-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_auto_20200806_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplacesettings',
            name='menu_url_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='marketplacesettings',
            name='menu_url_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='URL 2'),
        ),
        migrations.AlterField(
            model_name='marketplacesettings',
            name='menu_url_3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='URL 3'),
        ),
    ]
