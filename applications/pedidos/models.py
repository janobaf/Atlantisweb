from django.db import models
from django.conf import settings
from ..Mesas.models import mesa
from ..platos.models import Platos
from .managers import (PlatoManager,PedidosManager)
# Create your models here.
class PlatoPedidos(models.Model):
    plato = models.ForeignKey(Platos,unique=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observacion = models.CharField(max_length=150,null=True)
    objects=PlatoManager()

    def get_nombre_plato(self):
        return self.plato.Nombre_plato
    def __str__(self):
        return self.plato.Nombre_plato
class pedidos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mesa = models.OneToOneField(mesa,unique=True, on_delete=models.CASCADE)
    plato = models.ManyToManyField(PlatoPedidos,blank=True,unique=False)
    precio_total = models.FloatField(blank=True,null=True,default=0)
    objects=PedidosManager()
    
    