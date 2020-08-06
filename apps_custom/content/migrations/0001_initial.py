# Generated by Django 2.2.13 on 2020-08-04 08:05

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Content - Index',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='Post date')),
                ('intro', models.CharField(max_length=250)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Page standard',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContentTagIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('taggit.tag',),
        ),
        migrations.CreateModel(
            name='ContentAsso',
            fields=[
                ('contentpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.ContentPage')),
                ('site', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Association - Page de présentation',
            },
            bases=('content.contentpage',),
        ),
        migrations.CreateModel(
            name='ContentPartner',
            fields=[
                ('contentpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.ContentPage')),
                ('site', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Partenaire - Page de présentation',
            },
            bases=('content.contentpage',),
        ),
        migrations.CreateModel(
            name='MarketplaceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Marketplace Configuration',
            },
        ),
        migrations.CreateModel(
            name='ContentPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='content.ContentPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_contentpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentPageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='content.ContentPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentPageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.AddField(
            model_name='contentpage',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.ContentPageCategory'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='couverture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='content.ContentPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='ContentProjet',
            fields=[
                ('contentpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.ContentPage')),
                ('target', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Objectif de financement €')),
                ('asso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.ContentAsso')),
            ],
            options={
                'verbose_name': 'Projet - Page de présentation',
            },
            bases=('content.contentpage',),
        ),
        migrations.CreateModel(
            name='ContentIndexCategoryPage',
            fields=[
                ('contentindexpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.ContentIndexPage')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.ContentPageCategory')),
            ],
            options={
                'verbose_name': 'Content - Index par catégorie',
            },
            bases=('content.contentindexpage',),
        ),
    ]