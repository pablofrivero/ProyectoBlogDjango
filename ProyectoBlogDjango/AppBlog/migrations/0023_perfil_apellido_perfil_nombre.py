# Generated by Django 4.0.6 on 2022-09-03 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0022_perfil_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='apellido',
            field=models.CharField(default='generico', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(default='generico', max_length=200),
            preserve_default=False,
        ),
    ]