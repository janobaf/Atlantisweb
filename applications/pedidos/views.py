from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import  View,DeleteView
from .models import PlatoPedidos,pedidos
from ..Mesas.models import mesa
from ..platos.models import Platos
from ..usuarios.mixins import(MeseroPermisionMixin)


class CreatePedidoView(MeseroPermisionMixin,View):
    def get(self, request, *args, **kwargs):
        mesa_aux=mesa.objects.filter(numero_mesa=self.kwargs['numero_mesa'])
        user = self.request.user
        if mesa_aux.count()>0:
            try:
                pedido_aux = pedidos.objects.get(mesa=mesa_aux[0])
                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':pedido_aux.id}
                    )
                )
            except:
                pedido=pedidos.objects.addPedidos(
                    mesa=mesa_aux[0],
                    user=user
                )
                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':pedido.id}
                    )
                )
            
    def post(self,request,*args,**kwargs):
        mesa_aux=mesa.objects.filter(numero_mesa=self.kwargs['numero_mesa'])
        if mesa_aux.count()>0:
            try:
                pedido_aux = pedidos.objects.get(mesa=mesa_aux[0])
                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':pedido_aux.id}
                    )
                )
            except:
                pedido=pedidos.objects.addPedidos(
                    mesa=mesa_aux[0]
                )
                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':pedido.id}
                    )
                )

class AgregarPedidoView(MeseroPermisionMixin,View):

    def post(self,request,*args,**kwargs):
        
        platos_id=self.kwargs['pk']
        pedido_id=self.kwargs['idpedido']
        cantidad=self.request.POST.get('cantidad','')
        observaciones = self.request.POST.get('observaciones','')
        plato = Platos.objects.get(id=platos_id)
        
        
        pedido = pedidos.objects.get(id=pedido_id)

        if not observaciones:
            plato_pedidos = PlatoPedidos(plato=plato,cantidad=cantidad)
            plato_pedidos.save()
        else:
            plato_pedidos = PlatoPedidos.objects.addPlatoPedidos(
                plato=plato,
                cantidad=cantidad,
                observaciones=observaciones
            )

        precio_total=pedido.precio_total+(plato.precio_plato*float(cantidad))
        pedido.precio_total=precio_total
      
        pedido.save()
        pedido.plato.add(plato_pedidos)
    
        return HttpResponseRedirect(
            reverse(
                'platos_app:list-platos-pedido',
                kwargs={'idpedido':pedido_id}
            )
        )




class DeletePedidoView(View):
    def post(self,request,*args,**kwargs):
        idpedido=self.kwargs['idpedido']
        id_pedido_plato = self.request.POST.get('id')
        if id_pedido_plato:
            plato = PlatoPedidos.objects.filter(id=id_pedido_plato).exists()
            if plato:
                plato = PlatoPedidos.objects.get(id=id_pedido_plato)

                pedido = pedidos.objects.get(id=idpedido)
                precio_total=pedido.precio_total-(plato.plato.precio_plato*plato.cantidad)
                pedido.plato.remove(plato)
                pedido.precio_total=precio_total
                pedido.save()

                return HttpResponseRedirect(
                    reverse(
                        'platos_app:list-platos-pedido',
                        kwargs={'idpedido':idpedido}
                    )
                )
           
        return HttpResponseRedirect(
                reverse(
                    'platos_app:list-platos-pedido',
                    kwargs={'idpedido':idpedido}
                )
            )