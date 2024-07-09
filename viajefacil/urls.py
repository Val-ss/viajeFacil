from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('loginPage/', views.loginPage),
    path('logoutPage/', views.logoutPage),
    path('registro/', views.registerPage),
    path('destinos/',views.destinos),
    path('hoteles/', views.hoteles), 
    path('paquetes/', views.paquetes), 
    path('nuevoDestino/', views.nuevoDestino),
    path('nuevoDestino/<int:id>', views.nuevoDestino),
    path('detalle_hotel/<int:id>/', views.detalle_hotel, name='detalle_hotel'),
    path('nuevo_hotel/', views.nuevo_hotel),
    path('nuevo_hotel/<int:id>/', views.nuevo_hotel, name='nuevo_hotel'),
    path('hacerReserva/', views.reservas, name='hacerReserva'),
    path('seguridad/', views.seguridad),
    path('nuevoSeguridad/', views.nuevoSeguridad, name='nuevoSeguridad'),
    path('nuevoSeguridad/<int:id>/', views.nuevoSeguridad, name='nuevoSeguridad_id'),
    path('mapa/', views.mapa, name='mapa')
]