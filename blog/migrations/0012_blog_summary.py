# Generated by Django 5.0.1 on 2024-08-13 09:36

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_newsletter_social_links_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
