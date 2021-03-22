# Generated by Django 3.1.7 on 2021-03-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
    ]
