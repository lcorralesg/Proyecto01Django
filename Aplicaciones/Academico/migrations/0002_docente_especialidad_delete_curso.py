# Generated by Django 4.2 on 2023-05-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('idDocente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('fingreso', models.DateField()),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('idEspecialidad', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
