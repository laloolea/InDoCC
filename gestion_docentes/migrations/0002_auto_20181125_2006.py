# Generated by Django 2.1.2 on 2018-11-26 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_docentes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docente',
            old_name='user_name',
            new_name='username',
        ),
    ]
