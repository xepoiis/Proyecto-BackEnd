from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'perfiles', views.PerfilUsuarioViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'auditoria', views.HistorialAuditoriaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.inicio, name='inicio'),

    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('perfiles/', views.PerfilUsuarioListView.as_view(), name='perfil_list'),
    path('perfiles/<int:pk>/', views.PerfilUsuarioDetailView.as_view(), name='perfil_detail'),
    path('perfiles/crear/', views.PerfilUsuarioCreateView.as_view(), name='perfil_create'),
    path('perfiles/<int:pk>/editar/', views.PerfilUsuarioUpdateView.as_view(), name='perfil_update'),
    path('perfiles/<int:pk>/eliminar/', views.PerfilUsuarioDeleteView.as_view(), name='perfil_delete'),

    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/crear/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/editar/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/eliminar/', views.TicketDeleteView.as_view(), name='ticket_delete'),

    path('auditoria/', views.HistorialAuditoriaListView.as_view(), name='auditoria_list'),
    path('auditoria/<int:pk>/', views.HistorialAuditoriaDetailView.as_view(), name='auditoria_detail'),
    path('auditoria/crear/', views.HistorialAuditoriaCreateView.as_view(), name='auditoria_create'),
    path('auditoria/<int:pk>/editar/', views.HistorialAuditoriaUpdateView.as_view(), name='auditoria_update'),
    path('auditoria/<int:pk>/eliminar/', views.HistorialAuditoriaDeleteView.as_view(), name='auditoria_delete'),
]