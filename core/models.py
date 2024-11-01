from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    usuario = models.OneToOneField(User, verbose_name='profile', on_delete=models.CASCADE) 
    nome_completo = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


