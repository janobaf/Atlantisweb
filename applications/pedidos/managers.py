from django.db import models

class PlatoManager(models.Manager):
    def _createPlatos(self,plato,cantidad,**extra_fields):
        platos=self.model(plato=plato,cantidad=cantidad)
        platos.save(using=self.db)
        return platos
    
    def addPlatoPedidos(self,plato,cantidad,**extra_fields):
        return self._createPlatos(plato,cantidad,**extra_fields)
    
class PedidosManager(models.Manager):
    def _creacionPedidos(self,**extra_fields):
        pedidos=self.model(
           
            **extra_fields
        )
        pedidos.save(using=self.db)
        return pedidos
    def addPedidos(self,**extra_fields):
        return self._creacionPedidos(**extra_fields)