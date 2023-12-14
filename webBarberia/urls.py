"""
URL configuration for paginaWebBarberia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from loginRegistroUsuario import views as viewsAutenticacion
from extranet import views as viewsExtranet
from intranet import views as viewsIntranet


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", viewsExtranet.indice, name="index"),
    path("login/", viewsAutenticacion.login, name="loginUsuario"),
    path("registroUsuario/", viewsAutenticacion.registro, name="registroUsuario"),
    path("headerIntranet/",viewsIntranet.Header,name="headerIntranet"),
    path("sobreNosotros/",viewsIntranet.sobreNosotros,name="SobreNosotros"),
    path('agregarProductos/', viewsIntranet.agregar),
    path('eliminar3/<int:id>', viewsIntranet.eliminar3),
    path('actualizar/<int:id>', viewsIntranet.actualizar),
    path("servicios/", viewsIntranet.servicios, name="servicios"),
    path('confirmarCita/', viewsAutenticacion.confirmar_cita, name='confirmar_cita'),
    path("intranetBarbero/", viewsIntranet.intranetBarbero, name="intranetBarbero"),
    path("intranetCliente/", viewsIntranet.intranetCliente, name="intranetCliente"),
    path("agendarCita/",viewsIntranet.agendarCita, name ="agendarCita"),
]
