# Generated by Django 4.1.4 on 2023-01-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_student_profile_is_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile',
            name='Box_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='Postal_code',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='contact',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='firstname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='lastname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='middlename',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='town',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='Box_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='Postal_code',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='contact',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='firstname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='id_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='lastname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='middlename',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='trainer_profile',
            name='town',
            field=models.CharField(max_length=150),
        ),
    ]