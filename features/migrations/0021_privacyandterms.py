# Generated by Django 3.2 on 2023-06-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0020_auto_20230529_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyAndTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=100)),
                ('privacy_policy', models.TextField()),
                ('terms_and_condition', models.TextField()),
            ],
        ),
    ]
