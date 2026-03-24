from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('usuario', 'Usuario'),
        ('emprendedor', 'Emprendedor'),
        ('admin', 'Administrador'),
    )
        
    document = models.IntegerField(unique=True, blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    address = models.CharField(null=True, blank=True, max_length=200)
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='usuario')