from django.db import models

class MesasManager(models.Manager):
    def _createMesas(self,numero_mesa):
        mesas=self.model(
            numero_mesa=numero_mesa,
            ocupado=True
        )
        mesas.save(using=self.db)
        return mesas
    def createmesas(self,numero_mesa):
        return self._createMesas(numero_mesa)