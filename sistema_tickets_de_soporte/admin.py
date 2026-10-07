from django.contrib import admin
from .models import Categoria
from .models import PerfilUsuario
from .models import Ticket
from .models import HistorialAuditoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(PerfilUsuario)
admin.site.register(Ticket)
admin.site.register(HistorialAuditoria)