# Generated by Django 4.1.4 on 2023-01-09 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=150)),
                ('course_name', models.CharField(max_length=150)),
                ('module', models.CharField(max_length=50)),
                ('exam_body', models.CharField(choices=[('KNEC', 'KNEC'), ('NITA', 'NITA'), ('KASNEB', 'KASNEB')], max_length=50)),
                ('min_qualification', models.CharField(max_length=150)),
                ('duration', models.CharField(max_length=50)),
                ('intake', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=150)),
                ('department_code', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_code', models.CharField(max_length=150)),
                ('unit', models.CharField(max_length=150)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.course')),
            ],
            options={
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
    ]
