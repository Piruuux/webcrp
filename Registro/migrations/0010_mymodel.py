# Generated by Django 4.1.2 on 2023-03-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0009_auto_20230310_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='./assets/solcito.png')),
            ],
        ),
    ]
