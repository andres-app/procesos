from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Importa el decorador login_required
from django.utils.decorators import method_decorator
from .models import Proceso
from .forms import ProcesoForm, CustomUserCreationForm, ProcesoFilterForm
from django.db.models import Q  # Importar para las búsquedas avanzadas
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm  # Importa el formulario correcto

@login_required
def proceso_list(request):
    form = ProcesoFilterForm(request.GET)  # Inicializa el formulario con los datos GET
    procesos = Proceso.objects.all()

    # Filtrado basado en los campos del formulario
    if form.is_valid():
        if form.cleaned_data['numero']:
            procesos = procesos.filter(numero=form.cleaned_data['numero'])
        if form.cleaned_data['nombre']:
            procesos = procesos.filter(nombre__icontains=form.cleaned_data['nombre'])
        if form.cleaned_data['descripcion']:
            procesos = procesos.filter(descripcion__icontains=form.cleaned_data['descripcion'])

    context = {
        'form': form,
        'procesos': procesos
    }
    return render(request, 'pages/proceso_list.html', context)



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
 