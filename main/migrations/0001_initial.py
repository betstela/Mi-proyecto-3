# Generated by Django 3.0.8 on 2020-09-22 21:07

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
                ('Usuario_nombre', models.CharField(max_length=200)),
                ('Usuario_cedula', models.CharField(max_length=13)),
                ('Usurio_salida', models.DateTimeField(verbose_name='fecha de salida')),
            ],
        ),
    ]