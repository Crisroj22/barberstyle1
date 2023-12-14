from django.db import models

MASCULINO = "M"
FEMENINO = "F"
NO_BINARIO = "NB"
OTRO = "O"
PREFIERO_NO_DECIR = "PND"

opciones_genero = [
        (MASCULINO, "Masculino"),
        (FEMENINO, "Femenino"),
        (NO_BINARIO, "No Binario"),
        (OTRO, "Otro"),
        (PREFIERO_NO_DECIR, "Prefiero no decirlo")
    ]

class TipoUsuario(models.Model):
    id_tipo_usuario = models.IntegerField(
        primary_key = True,
        blank = False
    )
    nombre_tipo_usuario = models.CharField(
        max_length = 20
    )
    
    class Meta:
        db_table = "TipoUsuario"

class Usuario(models.Model):
    id_usuario = models.AutoField(
        primary_key = True
    )

    correo = models.CharField(
        max_length = 200, 
        blank = False
    )

    contrasena = models.CharField(
        max_length = 90, 
        blank = False
    )

    fk_id_tipo_usuario = models.ForeignKey(
        TipoUsuario,
        on_delete=models.CASCADE,
        default=1  # Establece el valor predeterminado en 1
    )
    
    class Meta:
        db_table = "Usuario"

class Cliente(models.Model):
    id_cliente = models.AutoField(
        primary_key = True
    )

    rut = models.CharField(
        max_length = 10, 
        blank = False
    )

    nombres = models.CharField(
        max_length = 120, 
        blank = False
    )

    genero = models.CharField(
        max_length = 3,
        choices = opciones_genero,
        default = MASCULINO,
    )

    numero_telefonico = models.CharField(
        max_length = 45
    )
    
    class Meta:
        db_table = "Cliente"

class Barbero(models.Model):
    id_barbero = models.AutoField(
        primary_key=True
    )

    rut = models.CharField(
        max_length = 10,
        blank = True
    )

    nombres = models.CharField(
        max_length = 120,
        blank = False
    )

    apellido_paterno = models.CharField(
        max_length = 120,
        blank = False
    )

    apellido_materno = models.CharField(
        max_length = 120,
        blank = False
    )

    genero = models.CharField(
        max_length = 3,
        choices = opciones_genero,
        default = MASCULINO,
    )

    numero_telefonico = models.CharField(
        max_length = 45
    )

    class Meta:
        db_table = "Barbero"
