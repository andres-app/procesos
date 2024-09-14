from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView  # Importar LoginView
from pages.views import proceso_list  # Asegúrate de importar la vista correcta

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),  # Vista de inicio de sesión
    path('home/', proceso_list, name='home'),  # Página de inicio después de iniciar sesión
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación de Django
    path('pages/', include('pages.urls')),  # Incluye todas las URLs de la aplicación 'pages'
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
