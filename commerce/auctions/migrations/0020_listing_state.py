# Generated by Django 3.0.8 on 2020-07-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20200710_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]