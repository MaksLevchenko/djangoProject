# Generated by Django 4.1.7 on 2023-02-17 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Django_Stripe_Api', '0005_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
    ]