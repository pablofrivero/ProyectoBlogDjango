# Generated by Django 4.0.6 on 2022-09-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0021_alter_post_creadopor'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='link',
            field=models.CharField(default='hola', max_length=200),
            preserve_default=False,
        ),
    ]
