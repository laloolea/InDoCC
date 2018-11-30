# Generated by Django 2.1.2 on 2018-11-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181127_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('admin', 'tiene acceso ilimitado'), ('docente', 'se limita a modificar unicamente su informacion')),
                'managed': False,
            },
        ),
    ]