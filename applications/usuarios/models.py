from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    administrador='A'
    mesero ='M'
    cocinero ='c'
    choices_roles=(
    (administrador,'administrador'),
    (mesero,'mesero'),
    (cocinero,'Cocinero')

    )

    choices_genero=(

        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros')
    )
    username = models.CharField(max_length=150,unique=True,blank=False)
    email = models.EmailField(blank=False)
    nombres = models.CharField(max_length=150,blank=False)
    apellidos = models.CharField(max_length=50,blank=False)
    genero = models.CharField(max_length=1, choices=choices_genero, blank=False)
    roles_usuario= models.CharField(max_length=1,choices=choices_roles,default='M')
    codregistro = models.CharField(max_length=6, blank=True)
    imagen = models.ImageField(upload_to='Usuarios')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos