# Generated by Django 4.1.1 on 2022-11-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_remove_template_category_remove_template_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
