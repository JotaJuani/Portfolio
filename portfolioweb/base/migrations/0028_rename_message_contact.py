# Generated by Django 5.0.6 on 2024-11-28 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_country_mapped_answer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Contact',
        ),
    ]
