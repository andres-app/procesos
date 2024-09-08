from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home_view, SignUpView, proceso_list, proceso_detail, proceso_create, proceso_update, proceso_delete

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Ruta de logout
    path('procesos/', proceso_list, name='proceso_list'),
    path('procesos/<int:pk>/', proceso_detail, name='proceso_detail'),
    path('procesos/new/', proceso_create, name='proceso_create'),
    path('procesos/<int:pk>/edit/', proceso_update, name='proceso_update'),
    path('procesos/<int:pk>/delete/', proceso_delete, name='proceso_delete'),
]

