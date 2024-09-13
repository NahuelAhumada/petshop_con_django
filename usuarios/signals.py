from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import Cliente

@receiver(post_save, sender=User)
def create_cliente(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(usuario=instance)
        print("Se han creado los datos de usuario")

@receiver(post_save, sender=User)
def update_perfil(sender, instance, created, **kwargs):
    if created==False:
        instance.cliente.save()
        print("perfil actualizado")
