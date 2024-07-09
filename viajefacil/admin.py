from django.contrib import admin

# Register your models here.

from . models import Destino
from . models import Hotel
from . models import Reserva_hotel
from . models import Seguridad
from . models import Paquete
from . models import Comments





admin.site.register(Destino)
admin.site.register(Hotel)
admin.site.register(Reserva_hotel)
admin.site.register(Seguridad)
admin.site.register(Paquete)
admin.site.register(Comments)



