# Generated by Django 5.0.6 on 2024-11-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='answer',
            field=models.CharField(choices=[('Argentina', 'Argentina'), ('Brazil', 'Brazil'), ('United States', 'United States'), ('Canada', 'Canada'), ('Uruguay', 'Uruguay'), ('Italy', 'Italy')], max_length=200),
        ),
    ]
