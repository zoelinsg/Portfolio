# Generated by Django 5.1.5 on 2025-01-15 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='thumbnail',
        ),
    ]
