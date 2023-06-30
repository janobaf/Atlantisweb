from django.urls import path

from . import views

app_name = "pedidos_app"

urlpatterns = [
    path(
        'pedidos-add/<numero_mesa>', 
                views.CreatePedidoView.as_view(),
                name='addpedido'
        ),
    path(
        'pedidos-add-platos/<pk>/<idpedido>',
        views.AgregarPedidoView.as_view(),
        name="pedidos-add-platos"
    ),
    path(
        'pedidos-add-platos/<idpedido>',
        views.DeletePedidoView.as_view(),
        name="delete_pedido_plato"
    )

]

