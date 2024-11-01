from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def cria_profile(sender, instance, created, **kwargs):
    """
    sender -> Subject (Objeto que está sendo observado pelos Observadores)
    
    instance -> Objeto que será manipulado (Observador)

    created -> Boolean (Apenas verdadeiro quando criamos um novo Observador)
    """
    if created:
        Profile.objects.create(usuario=instance)
    else:
        if not hasattr(instance, "profile"):
            Profile.objects.create(usuario=instance)


post_save.connect(receiver=cria_profile, sender=User)