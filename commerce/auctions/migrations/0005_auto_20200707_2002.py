# Generated by Django 3.0.8 on 2020-07-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200707_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='URL_image',
            field=models.URLField(max_length=300),
        ),
    ]
