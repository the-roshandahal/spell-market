# Generated by Django 4.1.1 on 2022-11-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0013_alter_template_template_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
