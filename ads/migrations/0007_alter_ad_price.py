# Generated by Django 4.0.2 on 2022-02-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
    ]
