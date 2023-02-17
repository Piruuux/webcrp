# Generated by Django 3.0.1 on 2023-02-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('apellido', models.CharField(max_length=40, null=True)),
                ('genero', models.CharField(max_length=40, null=True)),
                ('fecha_de_nacimiento', models.DateField(null=True)),
                ('pais', models.CharField(max_length=40, null=True)),
                ('estado', models.CharField(max_length=40, null=True)),
                ('dni', models.IntegerField(null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('grupo_de_running', models.CharField(max_length=40, null=True)),
                ('talle_de_remera', models.CharField(max_length=40, null=True)),
                ('categoria', models.CharField(max_length=40, null=True))
            ],
        ),
    ]
