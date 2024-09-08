from django.urls import path
from .views import home, proceso_list, proceso_detail, proceso_create, proceso_update, proceso_delete, SignUpView

urlpatterns = [
    path('', home, name='home'),  # Agrega la ruta para la vista home
    path('signup/', SignUpView.as_view(), name='signup'),  # URL para la vista de registro de usuarios
    path('procesos/', proceso_list, name='proceso_list'),
    path('procesos/<int:pk>/', proceso_detail, name='proceso_detail'),
    path('procesos/new/', proceso_create, name='proceso_create'),
    path('procesos/<int:pk>/edit/', proceso_update, name='proceso_update'),
    path('procesos/<int:pk>/delete/', proceso_delete, name='proceso_delete'),
]
