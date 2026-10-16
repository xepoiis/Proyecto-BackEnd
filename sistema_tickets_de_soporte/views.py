from rest_framework import viewsets
from django.shortcuts import render
from .models import Categoria, PerfilUsuario, Ticket, HistorialAuditoria
from .serializer import CategoriaSerializer, PerfilUsuarioSerializer, TicketSerializer, HistorialAuditoriaSerializer

def index(request):
    return render(request, 'index.html')

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class HistorialAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = HistorialAuditoria.objects.all()
    serializer_class = HistorialAuditoriaSerializer