# Generated by Django 4.0.6 on 2022-08-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0014_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
