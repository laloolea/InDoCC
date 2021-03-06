# Generated by Django 2.1.2 on 2018-11-28 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('pregunta', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
        migrations.CreateModel(
            name='PreguntaCerrada',
            fields=[
                ('pregunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Pregunta')),
                ('respuesta', models.BooleanField(default=False)),
            ],
            bases=('home.pregunta',),
        ),
        migrations.CreateModel(
            name='PreguntaMultiple',
            fields=[
                ('pregunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Pregunta')),
                ('respuesta', models.TextField()),
            ],
            bases=('home.pregunta',),
        ),
    ]
