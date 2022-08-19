# Generated by Django 4.0.6 on 2022-08-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('fechaDeEstreno', models.DateField()),
                ('descripcion', models.CharField(max_length=5000)),
                ('imagen', models.CharField(max_length=50)),
                ('fechaDeCreacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=5000)),
                ('imagen', models.CharField(max_length=50)),
                ('fechaDeCreacion', models.DateTimeField(auto_now_add=True)),
                ('pelicula_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppBlog.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=5000)),
                ('usuario', models.CharField(max_length=40)),
                ('fechaDeCreacion', models.DateTimeField(auto_now_add=True)),
                ('pelicula_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppBlog.pelicula')),
            ],
        ),
    ]
