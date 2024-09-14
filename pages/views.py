from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Proceso, Evento
from .forms import ProcesoForm, CustomUserCreationForm, ProcesoFilterForm, EventoForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

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

@method_decorator(login_required, name='dispatch')
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def home_view(request):
    # Asegúrate de que 'home.html' exista en tu directorio 'templates'
    return render(request, 'home.html')

# Vistas para Eventos
@login_required
def evento_list(request, proceso_id):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    eventos = Evento.objects.filter(proceso=proceso)
    return render(request, 'pages/evento_list.html', {'eventos': eventos, 'proceso': proceso})

@login_required
def evento_detail(request, proceso_id, pk):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    evento = get_object_or_404(Evento, pk=pk, proceso=proceso)
    return render(request, 'pages/evento_detail.html', {'evento': evento, 'proceso': proceso})

@login_required
def evento_create(request, proceso_id):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.proceso = proceso  # Asigna el proceso automáticamente
            evento.save()
            return redirect('evento_list', proceso_id=proceso.id)
    else:
        form = EventoForm()
    return render(request, 'pages/evento_form.html', {'form': form, 'proceso': proceso})

@login_required
def evento_update(request, proceso_id, pk):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    evento = get_object_or_404(Evento, pk=pk, proceso=proceso)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list', proceso_id=proceso.id)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'pages/evento_form.html', {'form': form, 'evento': evento, 'proceso': proceso})

@login_required
def evento_delete(request, proceso_id, pk):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    evento = get_object_or_404(Evento, pk=pk, proceso=proceso)
    if request.method == "POST":
        evento.delete()
        return redirect('evento_list', proceso_id=proceso.id)
    return render(request, 'pages/evento_confirm_delete.html', {'evento': evento, 'proceso': proceso})
