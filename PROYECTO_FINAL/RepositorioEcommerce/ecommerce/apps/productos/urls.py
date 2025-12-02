
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('listar/', views.Listar_Productos, name = 'path_listar_productos'),

    #DETALLE DE UN PRODUCTO CON FUNCION (VBF)
    #path('detalle/<int:pk>', views.Detalle_Producto_Funcion, name = 'path_detalle_producto'),

    #DETALLE DE UN PRODUCTO CON UNA CLASE (VBC)
    path('detalle/<int:pk>', views.Detalle_Producto_Clase.as_view(), name = 'path_detalle_producto'),
    
    #ABM
    path('crear/', views.Crear_Producto.as_view(),name = 'path_crear_producto'),
    path('modificar/<int:pk>', views.Modificar_Producto.as_view(),name = 'path_modificar_producto'),
    path('Eliminar/<int:pk>', views.Eliminar_Producto.as_view(), name = 'path_eliminar_producto'),

    #RUBROS
    path('rubros/', views.Listar_Rubros, name = 'path_listar_rubros'),
    path('productosxrubro/<int:pk>', views.Filtro_Rubro, name = 'path_filtrados_rubro'),
]