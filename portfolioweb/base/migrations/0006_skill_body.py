# Generated by Django 5.0.6 on 2024-08-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_title_skill_name_remove_skill_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
