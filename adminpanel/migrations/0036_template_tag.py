# Generated by Django 3.2 on 2022-12-07 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0035_rename_tags_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.tag'),
        ),
    ]
