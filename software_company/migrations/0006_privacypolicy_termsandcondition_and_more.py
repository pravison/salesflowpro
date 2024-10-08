# Generated by Django 5.0.1 on 2024-02-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_company', '0005_service_service_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TermsAndCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='companyinfor',
            name='geoloction_pin',
            field=models.URLField(blank=True, null=True),
        ),
    ]
