# forms.py

from django import forms
from .models import Reserva_hotel

class ReservaHotelForm(forms.ModelForm):
    class Meta:
        model = Reserva_hotel
        fields = '__all__'  # Incluye todos los campos del modelo en el formulario
