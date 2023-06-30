from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import(ListView,DeleteView,UpdateView)
from django.views.generic.edit import (FormView)

from django.db.models import Value ,CharField

from .models import Platos
from .forms import CreacionPlatosForm,ActualizarPlatosForm
from ..usuarios.mixins import AdministradorPermisionMixin,MeseroPermisionMixin
from ..pedidos.models import pedidos
# Create your views here.
class PlatosAddView(AdministradorPermisionMixin,FormView):
    template_name="platos/platosadd.html"
    form_class=CreacionPlatosForm
    success_url="/"
    
    def form_valid(self, form) :

        Platos.objects.CreatePlatosAdd(

            form.cleaned_data["Nombre_plato"],
            form.cleaned_data["precio_plato"],
            form.cleaned_data["categoria"],
            form.cleaned_data["imagen"]
        )
        
        return HttpResponseRedirect(
            reverse(
                'platos_app:list-platos',
               
            )
        )

    
class ListarPlatosView(MeseroPermisionMixin,ListView):
    template_name="platos/list-platos.html"
    model=Platos
    paginate_by=3
    context_object_name= 'plato'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        if self.kwargs:
            id_pedido=self.kwargs['idpedido']
            
            context['idpedido'] = id_pedido
            pedido=pedidos.objects.get(id=id_pedido)
            context['pedidos']= pedido
            context['plato_pedido']=pedido.plato.all()
            
        return context    


    def get_queryset(self):
        categoria_id=self.request.GET.get('categoria','')
        if categoria_id:
            if 0<=int(categoria_id)<8 :
                queryset=Platos.objects.ListPlatosCategoria(categoria_id)
                queryset=queryset.annotate(categorias = Value(categoria_id,output_field=CharField()))

            else :
                
                queryset=Platos.objects.all()

        else:
            queryset=Platos.objects.all()
        
          

        return queryset
    

class EliminarPlatoDeleteView(DeleteView):
    model = Platos
    success_url = reverse_lazy('platos_app:list-platos')


class ActualizarPlatosUpdateView(UpdateView):
    model = Platos
    template_name = "platos/update-platos.html"
    form_class=ActualizarPlatosForm
    success_url = reverse_lazy('platos_app:list-platos')

