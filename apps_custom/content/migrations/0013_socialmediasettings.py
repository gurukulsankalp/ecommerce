# Generated by Django 2.2.13 on 2020-08-05 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('content', '0012_delete_marketplaceconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_ca_marche', models.ForeignKey(blank=True, help_text='Lien vers la page de description du concept', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='content.ContentPage')),
                ('couverture_marketplace', models.ForeignKey(blank=True, help_text='Couverture de la marketplace', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
