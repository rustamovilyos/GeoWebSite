# Generated by Django 4.2 on 2023-04-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Geo', '0004_oceans_country_capital_country_climate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
