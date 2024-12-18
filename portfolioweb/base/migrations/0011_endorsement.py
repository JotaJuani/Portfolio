# Generated by Django 5.0.6 on 2024-10-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_message_remove_tag_email_remove_tag_is_read_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
