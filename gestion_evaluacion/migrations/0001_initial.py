# Generated by Django 2.1.1 on 2018-12-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hay_evaluacion_estudiantes', models.BooleanField(default=False)),
                ('Descripcion_evaluacion_estudiantes', models.TextField(blank=True, default='', null=True)),
                ('Hay_mecanismos_evaluacion', models.BooleanField(default=False)),
                ('Esta_reglamentado_mecanismos', models.BooleanField(default=False)),
                ('Descripcion_mecanismos', models.TextField(blank=True, default='', null=True)),
                ('Grupo_colegiado', models.BooleanField(default=False)),
                ('Descripcion_gruposColegiados', models.TextField(blank=True, default='', null=True)),
                ('Estudiantes', models.BooleanField(default=False)),
                ('Descripcion_estudiantes', models.TextField(blank=True, default='', null=True)),
                ('Otras_instancias', models.BooleanField(default=False)),
                ('Descripcion_instancias', models.TextField(blank=True, default='', null=True)),
                ('Hay_difusion', models.BooleanField(default=False)),
                ('Tipo_difusion', models.TextField(blank=True, default='', null=True)),
                ('Descripcion_entrega', models.TextField(blank=True, default='', null=True)),
                ('Hay_criterios', models.BooleanField(default=False)),
                ('Criterios_principales', models.TextField(blank=True, default='', null=True)),
                ('Hay_programa_estimulos', models.BooleanField(default=False)),
                ('DescripcionDifusion', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
