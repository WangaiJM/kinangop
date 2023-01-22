# Generated by Django 4.1.4 on 2023-01-19 18:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]