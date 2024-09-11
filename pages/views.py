from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Importa el decorador login_required
from django.utils.decorators import method_decorator
from .models import Proceso
from .forms import ProcesoForm, CustomUserCreationForm
from django.db.models import Q  # Importar para las búsquedas avanzadas
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm  # Importa el formulario correcto

@login_required
def proceso_list(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda del parámetro de consulta
    if query:
        # Filtrar los procesos según el término de búsqueda en 'nombre' o 'descripcion'
        procesos = Proceso.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    else:
        procesos = Proceso.objects.all()
    
    return render(request, 'pages/proceso_list.html', {'procesos': procesos})



@login_required
def proceso_detail(request, pk):
    proceso = get_object_or_404(Proceso, pk=pk)
    return render(request, 'pages/proceso_detail.html', {'proceso': proceso})

@login_required
def proceso_create(request):
    if request.method == "POST":
        form = ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proceso_list')
    else:
        form = ProcesoForm()
    return render(request, 'pages/proceso_form.html', {'form': form})

@login_required
def proceso_update(request, pk):
    proceso = get_object_or_404(Proceso, pk=pk)
    if request.method == "POST":
        form = ProcesoForm(request.POST, instance=proceso)
        if form.is_valid():
            form.save()
            return redirect('proceso_list')
    else:
        form = ProcesoForm(instance=proceso)
    return render(request, 'pages/proceso_form.html', {'form': form})

@login_required
def proceso_delete(request, pk):
    proceso = get_object_or_404(Proceso, pk=pk)
    if request.method == "POST":
        proceso.delete()
        return redirect('proceso_list')
    return render(request, 'pages/proceso_confirm_delete.html', {'proceso': proceso})

@method_decorator(login_required, name='dispatch')  # Protege la vista de registro
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def home(request):
    procesos = Proceso.objects.all()  # Obtener todos los procesos
    return render(request, 'home.html', {'procesos': procesos})

def home_view(request):
    # Asegúrate de que 'home.html' exista en tu directorio 'templates'
    return render(request, 'home.html')  
 