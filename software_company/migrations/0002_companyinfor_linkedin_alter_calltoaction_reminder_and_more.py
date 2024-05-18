# Generated by Django 5.0.1 on 2024-02-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfor',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calltoaction',
            name='reminder',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='statistic_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial_name',
            field=models.CharField(max_length=100),
        ),
    ]
