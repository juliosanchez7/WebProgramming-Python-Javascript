# Generated by Django 3.0.8 on 2020-07-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200708_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Product',
            field=models.ManyToManyField(blank=True, related_name='user', to='auctions.Listing'),
        ),
    ]