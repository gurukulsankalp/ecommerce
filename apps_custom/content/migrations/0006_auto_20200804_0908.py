# Generated by Django 2.2.13 on 2020-08-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20200804_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentproducttag',
            name='product',
        ),
        migrations.AlterField(
            model_name='contentproducttag',
            name='tag',
            field=models.CharField(max_length=30),
        ),
    ]
