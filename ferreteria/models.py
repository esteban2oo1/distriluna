from django.db import models
from django.utils import timezone

class Usuarios(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=10, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class TiposNovedades(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Novedades(models.Model):
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    dias_acumulados = models.IntegerField(default=0)
    tipoNovedad = models.ForeignKey(TiposNovedades, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=155, null=True, blank=True)

    def __str__(self):
        return f"{self.tipoNovedad}: {self.descripcion}"
    
class Usuarios_Novedades(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    novedad = models.ForeignKey(Novedades, on_delete=models.CASCADE)

    def total_dias(self):
        return (self.novedad.fecha_finalizacion - self.novedad.fecha_inicio).days + 1 

    def dias_restantes(self):
        dias_acumulados = self.novedad.dias_acumulados
        total_dias = self.total_dias()
        dias_restantes = total_dias - dias_acumulados
        return max(dias_restantes, 0)
    
