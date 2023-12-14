from django.shortcuts import render
from django.http import HttpResponse
from loginRegistroUsuario.models import Cliente, Usuario
from intranet.models import Cita
from django.shortcuts import render, redirect

def login(request):
    return render(request, '../templates/autenticacion/inicioSesion.html')

def registro(request):
    return render(request, '../templates/autenticacion/registroCliente.html')
# Create your views here.
def confirmar_cita(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST['nombre']
        email = request.POST['email']
        fecha_cita = request.POST['fecha']
        servicio_seleccionado = request.POST['servicio']  # Asegúrate de tener este campo en tu formulario

        # Crear Cliente
        cliente = Cliente.objects.create(
            nombres=nombre,
            correo=email,
        )

        usuario_existente = Usuario.objects.filter(correo=email).first()
        if not usuario_existente:
            usuario = Usuario.objects.create(
                correo=email,
                contrasena='una_contrasena_segura' 
            )
            cliente.id_usuario = usuario
            cliente.save()

        # Crear Cita
        cita = Cita.objects.create(
            id_cliente=cliente,
            servicio=servicio_seleccionado,
            hora_agendada=fecha_cita,
            # Otros campos de la Cita...
        )

        # Redirigir a la página de confirmación
        return render(request, 'confirmacion.html', {'cita': cita})

    return redirect('servicios')