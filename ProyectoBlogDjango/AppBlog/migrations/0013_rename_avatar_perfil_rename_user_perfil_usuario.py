# Generated by Django 4.0.6 on 2022-08-27 15:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppBlog', '0012_rename_profile_avatar_rename_usuario_avatar_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatar',
            new_name='Perfil',
        ),
        migrations.RenameField(
            model_name='perfil',
            old_name='user',
            new_name='usuario',
        ),
    ]
