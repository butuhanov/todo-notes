# Generated by Django 3.1.7 on 2021-03-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='repo_link',
            field=models.URLField(blank=True),
        ),
    ]