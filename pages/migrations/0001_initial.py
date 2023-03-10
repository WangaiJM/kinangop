# Generated by Django 4.1.5 on 2023-01-30 13:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='board_of_governor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/bog')),
            ],
            options={
                'verbose_name_plural': 'Board of Governors',
            },
        ),
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='carousel/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/dean')),
            ],
            options={
                'verbose_name_plural': 'Dean of Students',
            },
        ),
        migrations.CreateModel(
            name='dprincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/dean')),
            ],
            options={
                'verbose_name_plural': 'Deputy Principal',
            },
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='guidance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/dean')),
            ],
            options={
                'verbose_name_plural': 'Guidance and Counselling',
            },
        ),
        migrations.CreateModel(
            name='principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/principal')),
            ],
        ),
        migrations.CreateModel(
            name='procument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/dean')),
            ],
        ),
        migrations.CreateModel(
            name='registrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/dean')),
            ],
        ),
        migrations.CreateModel(
            name='service_charter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('charter', models.FileField(upload_to='charter/')),
            ],
            options={
                'verbose_name_plural': 'Service Charter',
            },
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
