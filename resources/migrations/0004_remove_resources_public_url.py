# Generated by Django 4.2.2 on 2023-06-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_resources_image_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='public_url',
        ),
    ]
