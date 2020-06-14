from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Necessário um email válido'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Usuarios(PermissionsMixin, AbstractBaseUser):
    nome = models.CharField(max_length=255, blank=False)
    sobrenome = models.CharField(max_length=255, blank=False)
    email = models.EmailField(unique=True, max_length=255)
    reset_pass = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

    def __str__(self):
        return "{} | {}".format(self.id, self.email)

    def __repr__(self):
        return "{} | {}".format(self.id, self.email)

    @property
    def ativo_human(self):
        return 'Sim' if self.is_active else 'Não'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'