# Generated by Django 2.2.13 on 2020-08-04 08:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('content', '0002_producttag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='content.ContentPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_contentproducttag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='ProductTag',
        ),
        migrations.AlterField(
            model_name='contentpagetag',
            name='content_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='catalogue.Product'),
        ),
    ]