# Generated by Django 2.1.2 on 2018-11-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_docentes', '0002_auto_20181125_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='first_name',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='docente',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]