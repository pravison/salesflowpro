# Generated by Django 5.0.1 on 2024-10-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(default='salesflow@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
