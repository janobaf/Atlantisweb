from typing import Any
from django.shortcuts import redirect
from django.urls import  reverse,reverse_lazy
from django.views.generic import(View,ListView,DeleteView)
from .models import mesa
from .forms import CreateMesasForms
from ..usuarios.mixins import MeseroPermisionMixin
from ..pedidos.models import pedidos
from django.contrib import messages


class AddMesaView1(MeseroPermisionMixin,View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        numero_mesa=self.request.POST.get('numero_mesa')
        pk_Existente  = mesa.objects.get(numero_mesa=numero_mesa)
        if pk_Existente:
            context['errores'] = {'existe':True}

        return context
    
    def post(self, request, *args, **kwargs) :
        numero_mesa = self.request.POST.get('numero_mesa')
       
        if numero_mesa:
            form = CreateMesasForms(request.POST)
            if form.is_valid():
                mesa.objects.createmesas(numero_mesa)
                return redirect(
                                'pedidos_app:addpedido',
                                numero_mesa=numero_mesa)
                    
                
            else :
                for field, errors  in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")

            return redirect('mesas_app:list-mesas')
class UpdateMesa(MeseroPermisionMixin,View):
    def post(self, request, *args, **kwargs) :
        id_mesa=self.kwargs['pk']
        id_mesa_update = self.request.POST.get('mesaupdate')
        mesa_aux = mesa.objects.get_or_create(numero_mesa=id_mesa)
        mesa_aux=mesa_aux[0]
        if mesa_aux:
            try:
                pedido=pedidos.objects.get(mesa__numero_mesa=id_mesa)
    
                mesa_aux.numero_mesa=id_mesa_update
                mesa_aux.save()
                pedido.mesa=mesa_aux
               
                pedido.save()
                print(pedido.mesa.numero_mesa)
                
                return redirect('mesas_app:list-mesas')
            except:
                return redirect('mesas_app:list-mesas')
            
        return redirect('mesas_app:list-mesas')      
    
class listMesasListView(MeseroPermisionMixin,ListView):
    model = mesa
    context_object_name="mesa"
    paginate_by=12
    template_name = "mesas/list-mesas.html"
    



class DeleteMesa(MeseroPermisionMixin,DeleteView):
    model = mesa
    success_url=reverse_lazy('mesas_app:list-mesas')