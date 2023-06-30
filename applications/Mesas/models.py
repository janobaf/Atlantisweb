from django.db import models
from .managers import MesasManager
# Create your models here.

class mesa(models.Model):
    numero_mesa = models.IntegerField(primary_key=True,unique=True)
    ocupado = models.BooleanField(default=False)
    objects=MesasManager()
    def get_numero_mesa(self):
        return self.numero_mesa
    
    def __str__(self):
        return str(self.numero_mesa)
    