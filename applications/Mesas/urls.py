from django.urls import path

from . import views

app_name = "mesas_app"

urlpatterns = [
  
    path(
        'list-mesas/',
        views.listMesasListView.as_view(),
        name="list-mesas"
    ),
    path(
        'mesasadd1/',
        views.AddMesaView1.as_view(),
        name="addmesas"
    ),
    path('delete-mesa/<pk>/',
         views.DeleteMesa.as_view(),
         name='delete'),
    path('update-mesa/<pk>/',
    views.UpdateMesa.as_view(),
    name='update')
]

