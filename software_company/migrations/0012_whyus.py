# Generated by Django 5.0.1 on 2024-03-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_company', '0011_compaarison'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('first_point_icon', models.CharField(max_length=100)),
                ('first_point_title', models.CharField(max_length=100)),
                ('first_point_overview', models.TextField(max_length=200)),
                ('second_point_icon', models.CharField(max_length=100)),
                ('second_point_title', models.CharField(max_length=100)),
                ('second_point_overview', models.TextField(max_length=200)),
                ('third_point_icon', models.CharField(max_length=100)),
                ('third_point_title', models.CharField(max_length=100)),
                ('third_point_overview', models.TextField(max_length=200)),
            ],
        ),
    ]
