# Generated by Django 4.1.1 on 2022-11-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0008_childcategory_created_childcategory_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='childcategory',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]