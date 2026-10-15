from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'perfiles', views.PerfilUsuarioViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'auditoria', views.HistorialAuditoriaViewSet)

urlpatterns = [
        path('', include(router.urls)),
]