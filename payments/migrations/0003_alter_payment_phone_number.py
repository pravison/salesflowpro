# Generated by Django 5.0.1 on 2024-10-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_email_payment_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
