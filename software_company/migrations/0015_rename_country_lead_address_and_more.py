# Generated by Django 5.0.1 on 2024-10-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_company', '0014_customerplan_customerinvoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='country',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='customerinvoice',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='lead',
            name='message',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
