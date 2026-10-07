from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

ahora = timezone.now

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=250, null=False)
    sla_horas = models.IntegerField(null=False)
    activa = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

class PerfilUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=25, null=False)
    departamento = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

class Ticket(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=500, null=False)
    estado = models.CharField(max_length=25, null=False)
    prioridad = models.CharField(max_length=25, null=False)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

class HistorialAuditoria(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    accion = models.CharField(max_length=100, null=False)
    estado_anterior = models.CharField(max_length=25, null=False)
    estado_nuevo = models.CharField(max_length=25, null=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)