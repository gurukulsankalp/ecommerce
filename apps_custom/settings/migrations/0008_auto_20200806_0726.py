# Generated by Django 2.2.13 on 2020-08-06 07:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_auto_20200806_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplacesettings',
            name='menu_url_1',
            field=wagtail.core.fields.StreamField([('label', wagtail.core.blocks.CharBlock(max_length=30, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False))], null=True),
        ),
        migrations.AddField(
            model_name='marketplacesettings',
            name='menu_url_2',
            field=wagtail.core.fields.StreamField([('label', wagtail.core.blocks.CharBlock(max_length=30, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False))], null=True),
        ),
        migrations.AddField(
            model_name='marketplacesettings',
            name='menu_url_3',
            field=wagtail.core.fields.StreamField([('label', wagtail.core.blocks.CharBlock(max_length=30, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False))], null=True),
        ),
    ]
