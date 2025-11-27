
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('listar/', views.Listar_Productos, name = 'path_listar_productos'),

    #DETALLE DE UN PRODUCTO CON FUNCION (VBF)
    #path('detalle/<int:pk>', views.Detalle_Producto_Funcion, name = 'path_detalle_producto'),

    #DETALLE DE UN PRODUCTO CON UNA CLASE (VBC)
    path('detalle/<int:pk>', views.Detalle_Producto_Clase.as_view(), name = 'path_detalle_producto')
    
]