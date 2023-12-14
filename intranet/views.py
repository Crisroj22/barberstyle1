from django.shortcuts import render, redirect
from intranet.models import Producto
from intranet.forms import FormBarbero, FormBodega
from django.shortcuts import get_object_or_404

# Create your views here.
def Header(request):
    productos = Producto.objects.all()
    data = {'productos':productos}
    return render(request, '../templates/footersYHeaders/headerIntranet.html',data)

def sobreNosotros(request):
    return render(request,"../templates/intranet/sobreNosotros.html")

def agregar(request):
    form = FormBodega()
    if request.method == 'POST' :
        form = FormBodega(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("headerIntranet")
    data = {'form' : form}
    return render(request, '../templates/footersYHeaders/agregarProductos.html', data)

def eliminar3(request, id):
    producto = Producto.objects.get(id_producto = id)
    producto.delete()
    return redirect('headerIntranet')

def agendarCita(request):
    return render(request,"../templates/intranet/agendarCita.html")

def servicios(request):
    return render(request,"../templates/intranet/servicios.html")

def intranetBarbero(request):
    return render(request,"../templates/intranet/intranetBarbero.html")

def intranetCliente(request):
    return render(request,"../templates/intranet/intranetCliente.html")

def actualizar(request, id):
    producto = Producto.objects.get(id_producto=id)
    if request.method == 'POST':
        form = FormBarbero(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("headerIntranet")
    else:
        form = FormBarbero(instance=producto)

    data = {'form': form}
    return render(request, '../templates/footersYHeaders/agregarProductos.html', data)


#def actualizar(request, id):
    producto = Producto.objects.get(id = id)
    form = FormBarbero(instance=producto)
    if request.method == 'POST' :
        form = FormBarbero(request.POST, instance=producto)
        if form.is_valid() :
            form.save()
        return redirect("headerIntranet")
    data = {'form' : form}
    return render(request, '../templates/footersYHeaders/agregarProductos.html', data)