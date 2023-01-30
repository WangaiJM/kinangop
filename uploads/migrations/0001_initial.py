# Generated by Django 4.1.5 on 2023-01-30 13:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='Notes/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.units')),
            ],
        ),
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='Notes/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.units')),
            ],
        ),
    ]
