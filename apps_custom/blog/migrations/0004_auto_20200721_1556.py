# Generated by Django 2.2.13 on 2020-07-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200720_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexcategorypage',
            options={'verbose_name': 'Blog - Index par catégorie'},
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='image_credit',
        ),
    ]