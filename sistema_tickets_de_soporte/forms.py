from django import forms
from .models import Categoria, PerfilUsuario, Ticket, HistorialAuditoria

ROLES_CHOICES = [
    ('Cliente', 'Cliente'),
    ('Tecnico', 'Tecnico'),
    ('Administrador', 'Administrador'),
]

ESTADOS_CHOICES = [
    ('Abierto', 'Abierto'),
    ('En Progreso', 'En Progreso'),
    ('Resuelto', 'Resuelto'),
    ('Cerrado', 'Cerrado'),
]

PRIORIDADES_CHOICES = [
    ('Baja', 'Baja'),
    ('Media', 'Media'),
    ('Alta', 'Alta'),
    ('Critica', 'Critica'),
]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'sla_horas', 'activa']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Soporte de Redes y Conectividad',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describa los tipos de incidencias cubiertas por esta categoria',
            }),
            'sla_horas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Tiempo maximo de resolucion en horas',
            }),
            'activa': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['usuario', 'rol', 'departamento']
        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'form-select',
            }),
            'rol': forms.Select(
                choices=ROLES_CHOICES,
                attrs={'class': 'form-select'},
            ),
            'departamento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Tecnologias de la Informacion',
            }),
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['categoria', 'creador', 'titulo', 'descripcion', 'estado', 'prioridad', 'activo']
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'creador': forms.Select(attrs={
                'class': 'form-select',
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Resumen breve de la incidencia reportada',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Detalle el problema, mensajes de error y pasos realizados',
            }),
            'estado': forms.Select(
                choices=ESTADOS_CHOICES,
                attrs={'class': 'form-select'},
            ),
            'prioridad': forms.Select(
                choices=PRIORIDADES_CHOICES,
                attrs={'class': 'form-select'},
            ),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class HistorialAuditoriaForm(forms.ModelForm):
    class Meta:
        model = HistorialAuditoria
        fields = ['ticket', 'accion', 'estado_anterior', 'estado_nuevo']
        widgets = {
            'ticket': forms.Select(attrs={
                'class': 'form-select',
            }),
            'accion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Escalamiento a soporte nivel 2',
            }),
            'estado_anterior': forms.Select(
                choices=ESTADOS_CHOICES,
                attrs={'class': 'form-select'},
            ),
            'estado_nuevo': forms.Select(
                choices=ESTADOS_CHOICES,
                attrs={'class': 'form-select'},
            ),
        }