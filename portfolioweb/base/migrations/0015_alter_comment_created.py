# Generated by Django 5.0.6 on 2024-10-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
