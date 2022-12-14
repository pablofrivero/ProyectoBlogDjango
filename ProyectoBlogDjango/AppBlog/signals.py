from django.db.models.signals import post_save
#Importo para la relacion con USER
from django.contrib.auth.models import User
from .models import Perfil
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.perfil.save()