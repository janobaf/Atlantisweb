from django.db import models
from .managers import PlatosManager
# Create your models here.

class Platos(models.Model):
    categoria_pltaos=(
                      ('0','Criollos'),
                      ('1','Ceviches'),
                      ('2','Especialidades'),
                      ('3','Chicharrones'),
                      ('4','Parrillas'),
                      ('5','postres'),
                      ('6','Gaseosas'),
                      ('7','TAPERS')
                      )
    id = models.BigAutoField(primary_key=True)
    Nombre_plato = models.CharField('Nombre_Plato', max_length=150,blank=False)
    precio_plato = models.FloatField('precio_plato',blank=False)
    categoria = models.CharField('Categoria', max_length=1,choices=categoria_pltaos)
    imagen = models.ImageField( upload_to='platos')
    objects= PlatosManager()
    def get_Nombre_plato(self):
        return self.Nombre_plato
    
    def __str__(self) -> str:
        return 'id : '+str(self.id)+' '+'Nombre Plato: '+self.Nombre_plato