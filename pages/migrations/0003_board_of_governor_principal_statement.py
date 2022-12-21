# Generated by Django 4.1.4 on 2022-12-21 11:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='board_of_governor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/principal')),
            ],
        ),
        migrations.CreateModel(
            name='principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/principal')),
            ],
        ),
        migrations.CreateModel(
            name='statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', ckeditor.fields.RichTextField()),
                ('mission', ckeditor.fields.RichTextField()),
                ('core_values', ckeditor.fields.RichTextField()),
                ('quality_policy_statement', ckeditor.fields.RichTextField()),
                ('motto', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
