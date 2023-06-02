# Generated by Django 3.2 on 2023-05-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0018_sitemapentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=100)),
                ('home_meta_title', models.TextField()),
                ('home_meta_description', models.TextField()),
                ('home_meta_keywords', models.TextField()),
                ('about_meta_title', models.TextField()),
                ('about_meta_description', models.TextField()),
                ('about_meta_keywords', models.TextField()),
                ('contact_meta_title', models.TextField()),
                ('contact_meta_description', models.TextField()),
                ('contact_meta_keywords', models.TextField()),
                ('blogs_meta_title', models.TextField()),
                ('blogs_meta_description', models.TextField()),
                ('blogs_meta_keywords', models.TextField()),
                ('themes_meta_title', models.TextField()),
                ('themes_meta_description', models.TextField()),
                ('themes_meta_keywords', models.TextField()),
            ],
        ),
    ]