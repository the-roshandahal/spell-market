# Generated by Django 4.1.1 on 2022-11-27 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0025_promocode_rename_blogs_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='testimonial',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]