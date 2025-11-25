from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , views.Home, name = 'path_home'),
    path('contacto/', views.Contacto, name = 'path_contacto'),

    #enlazar a la url de las app
    path('productos/', include('productos.urls')),
    
]
