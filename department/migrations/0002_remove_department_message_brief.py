# Generated by Django 4.1.5 on 2023-01-30 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department_message',
            name='brief',
        ),
    ]