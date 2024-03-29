# Generated by Django 4.1.1 on 2022-11-18 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
        ('features', '0002_cart_downloads_tag_token_template_template_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='category',
        ),
        migrations.RemoveField(
            model_name='template',
            name='tag',
        ),
        migrations.AlterField(
            model_name='cart',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.template'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
    ]
