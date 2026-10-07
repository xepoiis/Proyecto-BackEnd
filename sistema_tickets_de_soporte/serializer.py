from rest_framework import serializers

from .models import Categoria
from .models import PerfilUsuario
from .models import Ticket
from .models import HistorialAuditoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ('__all__')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('__all__')

class HistorialAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAuditoria
        fields = ('__all__')