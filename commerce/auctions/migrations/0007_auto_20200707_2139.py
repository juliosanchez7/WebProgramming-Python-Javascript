# Generated by Django 3.0.8 on 2020-07-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='Product',
        ),
        migrations.AddField(
            model_name='bids',
            name='Product',
            field=models.ManyToManyField(blank=True, related_name='Products', to='auctions.Listing'),
        ),
    ]
