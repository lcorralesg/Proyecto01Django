# Generated by Django 4.2 on 2023-05-31 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_docente_especialidad_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.PositiveIntegerField()),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.docente')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.especialidad')),
            ],
        ),
    ]