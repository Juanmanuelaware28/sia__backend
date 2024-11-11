# student_login/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo de usuario personalizado
class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    # Relacionar grupos y permisos con nombres únicos para evitar conflicto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='studentuser_set',  # Nombre único para evitar el conflicto
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='studentuser_permissions',  # Nombre único para evitar el conflicto
        blank=True
    )

    def __str__(self):
        return self.username
