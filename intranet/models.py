from django.db import models
from loginRegistroUsuario import models as models_registro_usuario

ACTIVO = "A"
INACTIVO = "I"

estado_cita = [
    (ACTIVO,"ACTIVO"),
    (INACTIVO,"INACTIVO")
]

class Cita(models.Model):
    id_cita = models.AutoField(
        primary_key = True
    )

    id_barbero = models.ForeignKey(
        models_registro_usuario.Barbero,
        db_column = 'fk_id_barbero', #renombra la columna para que no diga id_barbero_id
        on_delete = models.CASCADE
    )

    id_cliente = models.ForeignKey(
        models_registro_usuario.Cliente, 
        db_column = 'fk_id_cliente',
        on_delete=models.CASCADE
    )

    hora_agendada = models.DateTimeField(
        null = False,
        blank = False,
        verbose_name = 'Fecha agendada'
    )

    estado = models.CharField(
        max_length = 8,
        choices = estado_cita,
        default = ACTIVO
    )

    class Meta:
        db_table = "Cita"
    
class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(
        primary_key = True
    )

    nombre_metodo_pago = models.CharField(
        max_length = 45,
        blank = False
    )
    
    class Meta:
        db_table = "MetodoPago"
    
class Servicio(models.Model):
    id_servicio = models.AutoField(
        primary_key = True
    )

    descripcion = models.TextField(
        max_length=150,
        blank=False
    )

    duracion = models.CharField(
        max_length=45,
        blank=False
    )

    class Meta:
        db_table = "Servicio"
    
class Venta(models.Model):
    id_venta = models.AutoField(
        primary_key = True 
    )
    id_metodo_pago = models.IntegerField(
        
    )
    hora_fecha = models.TimeField(
        
    )
    total = models.CharField(
        max_length = 45 
    )
    
    class Meta:
        db_table = "Venta"
    
class CitaServicio(models.Model):
    id_cita = models.ForeignKey(
        Cita, 
        db_column = 'fk_id_cita',
        on_delete = models.CASCADE
    )

    id_servicio = models.ForeignKey(
        Servicio,
        db_column = 'fk_id_servicio',
        on_delete = models.CASCADE   
    )

    class Meta:
        db_table = "CitaServicio"
    
class Producto(models.Model):
    id_producto = models.AutoField(
        primary_key = True
    )

    nombre_producto = models.CharField(
        max_length = 45
    )

    descripcion = models.TextField(
        max_length = 150
    )

    precio = models.IntegerField(
    )

    stock = models.CharField(
        max_length = 45
    )
    
    class Meta:
        db_table = "Producto"
    
class ProductoVenta(models.Model):
    id_producto = models.ForeignKey(
        Producto,
        db_column = 'fk_id_producto',
        on_delete = models.CASCADE
    )

    id_venta = models.ForeignKey(
        Venta,
        db_column = 'fk_id_venta',
        on_delete = models.CASCADE
    )

    cantidad = models.IntegerField()

    class Meta:
        db_table = "ProductoVenta"

class CitaVenta(models.Model):
    id_cita = models.ForeignKey(
        Cita,
        db_column = 'fk_id_cita',
        on_delete = models.CASCADE
    )

    id_venta = models.ForeignKey(
        Venta,
        db_column = 'fk_id_venta',
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = "CitaVenta"