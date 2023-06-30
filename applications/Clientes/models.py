from django.db import models

# Create your models here.
class clientes(models.Model):
    dni = models.CharField(primary_key=True,verbose_name="dni", max_length=8)
    nombre_cliente = models.CharField('nombre_cliente', max_length=150,blank=False)
    ruc = models.CharField('ruc',max_length=13,blank=True)
    nombre_Empresa = models.CharField("nombre_empresa",max_length=150,blank=True)

    direcccion = models.CharField('direccion', max_length=150)
    

    def __str__(self):
        return self.nombre_cliente