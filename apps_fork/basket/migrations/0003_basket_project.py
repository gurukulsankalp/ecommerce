# Generated by Django 2.2.13 on 2020-07-28 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200721_1556'),
        ('basket', '0002_auto_20200720_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.BlogProjet'),
        ),
    ]