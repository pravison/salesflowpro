# Generated by Django 5.0.1 on 2024-03-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_company', '0009_rename_feaure1_pricing_feature1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='industry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='number_of_sales_reps',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
