# Generated by Django 5.0.6 on 2024-10-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_project_body_alter_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Fullstack', 'Fullstack'), ('Recruiter', 'Recruiter')], max_length=200),
        ),
    ]
