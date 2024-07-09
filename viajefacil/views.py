from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages




from . models import Destino
from . models import Hotel
from . models import Reserva_hotel
from . models import Seguridad
from . models import Paquete





# Create your views here.
def es_miembro_staff(user):
    return user.is_staff


def loginPage(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Se inició sesión correctamente.")
                return redirect('/')
            
        messages.error(request, "Usuario o contraseña incorrecto.")
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

def registerPage(request): 
    if(request.method == 'POST'):
        username = request.POST.get('username')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'La contraseñas no coinciden')
            return redirect('/registerPage')
        User.objects.create_user(username, first_name=name, last_name=last_name, email=email, password=password)
        return redirect('/loginPage')
    return render(request,'register.html')

def home(request):
    destino = Destino.objects.all()
    paquetes = Paquete.objects.all()
    context = {
        'paquetes': paquetes,
        'destino' : destino
    }
    return render(request, 'home.html', context)

def paquetes(request):
    paquetes = Paquete.objects.all()
    context = {
        'paquetes': paquetes,
        }
    return render(request, 'paquetes.html', context)


 


@login_required
@user_passes_test(es_miembro_staff)
def nuevoDestino(request, id=None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if(id is None):
            Destino.objects.create(
                titulo = request.POST.get('titulo'),
                descripcion = request.POST.get('descripcion'),
                precio = request.POST.get('precio')
            )
            messages.success(request, "Destino creado correctamente.")
            return redirect('/')
        else:
            p = Destino.objects.get(id = id)
            p.titulo = request.POST.get('titulo')
            p.descripcion = request.POST.get('descripcion')
            p.precio = request.POST.get('precio')
            p.save()
            messages.success(request, "Destino actualizado correctamente.")
            return redirect('/')

    context = {}
    if id is not None:
        destino = Destino.objects.get(id = id)
        context['destino'] = destino

    return render(request, 'nuevoDestino.html',context)

def destinos(request):
    destino = Destino.objects.all()
    return render(request, 'destinos.html', {'destino': destino})

def nuevo_hotel(request, id=None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if(id is None):
            Hotel.objects.create(
                nombre = request.POST.get('nombre'),
                descripcion = request.POST.get('descripcion'),
                habitacion = request.POST.get('habitacion'),
                ubicacion = request.POST.get('ubicacion'),
                precio = request.POST.get('precio')
            )
            messages.success(request, "Hotel creado correctamente.")
            return redirect('/')
        else:
            h = Hotel.objects.get(id = id)
            h.nombre = request.POST.get('nombre')
            h.descripcion = request.POST.get('descripcion')
            h.habitacion = request.POST.get('habitacion')
            h.precio = request.POST.get('precio')
            h.save()

    context = {}
    if id is not None:
        hotel = Hotel.objects.get(id = id)
        context['hotel'] = hotel

    return render(request, 'nuevo_hotel.html',context)

def hoteles(request):
    hotel = Hotel.objects.all()
    reserva = Reserva_hotel.objects.all()
    return render(request, 'hoteles.html', {'hotel' : hotel, 'reserva' : reserva})

def detalle_hotel(request, id):
    hotel = get_object_or_404(Hotel, id=id)  # Obtiene el hotel por su id
    context = {'hotel': hotel}  # Pasar hotel y posts en un solo diccionario
    return render(request, 'detalle_hotel.html', context)

def reservas(request):
    reserva = Reserva_hotel.objects.all()
    return render(request, 'hacerReserva.html', {'reserva': reserva})

def seguridad(request):
    seguridad = Seguridad.objects.all()  # Obtener todos los objetos de Seguridad
    context = {'seguridad': seguridad}
    return render(request, 'seguridad.html', context)

def nuevoSeguridad(request, id=None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if(id is None):
            Seguridad.objects.create(
                titulo = request.POST.get('titulo'),
                descripcion = request.POST.get('descripcion'),
                )
        else:
            s = Seguridad.objects.get(id = id)
            s.titulo = request.POST.get('titulo')
            s.descripcion = request.POST.get('descripcion')
            s.save()

    context = {}
    if id is not None:
        seguridad = Seguridad.objects.get(id = id)
        context['seguridad'] = seguridad

    return render(request, 'nuevoSeguridad.html',context)



def mapa(request):
    return render(request, 'mapa.html')