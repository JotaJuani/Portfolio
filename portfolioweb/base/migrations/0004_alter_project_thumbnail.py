# Generated by Django 5.0.6 on 2024-08-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_skill_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
