# Generated by Django 3.0.8 on 2020-07-07 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing',
            new_name='Listings',
        ),
    ]