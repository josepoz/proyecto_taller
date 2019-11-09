from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Propietario, Auto, Mecanico, Trabajo, Trabajo_mecanico
from .forms import AutoForm, TrabajoForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def propietario_list(request):
    propietarios = Propietario.objects.filter(fecha_registro__lte=timezone.now()).order_by('fecha_registro')
    return render(request, 'mecanica/propietarios_list.html', {'propietarios': propietarios})

#Autos=============================================
#==================================================
def auto_list(request):
    autos = Auto.objects.filter(fecha_registro__lte=timezone.now()).order_by('fecha_registro')
    return render(request, 'mecanica/autos_list.html', {'autos': autos})

def detalle_auto(request,pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'mecanica/auto_detail.html', {'auto': auto})

def auto_new(request):
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            auto = form.save(commit=False)
            auto.fecha_registro = timezone.now()
            auto.save()
            return redirect('detalle_auto', pk=auto.pk)
    else:
        form = AutoForm()
    return render(request, 'mecanica/auto_edit.html', {'form': form})
    # return render(request, 'blog/post_edit.html', {'form': form})

def auto_edit(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == "POST":
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            auto = form.save(commit=False)
            auto.fecha_registro = timezone.now()
            auto.save()
            return redirect('detalle_auto', pk=auto.pk)
    else:
        form = AutoForm(instance=auto)
    return render(request, 'mecanica/auto_edit.html', {'form': form})

#Mecacnicos
def mecanico_list(request):
    mecanicos = Mecanico.objects.all().order_by('nombre')
    return render(request, 'mecanica/mecanicos_list.html', {'mecanicos': mecanicos})

#Trabajos
#=============================================
#==================================================
def trabajo_list(request):
    trabajos = Trabajo.objects.all().order_by('fecha')
    return render(request, 'mecanica/trabajos_list.html', {'trabajos': trabajos})

def detalle_trabajo(request,pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    return render(request, 'mecanica/trabajo_detail.html', {'trabajo': trabajo})

def trabajo_new(request):
    if request.method == "POST":
        formulario = TrabajoForm(request.POST)
        if formulario.is_valid():
            trabajo = Trabajo.objects.create(auto_placas=formulario.cleaned_data['auto_placas'], trabajo_descripcion = formulario.cleaned_data['trabajo_descripcion'], costo_total = formulario.cleaned_data['costo_total'], estado = formulario.cleaned_data['estado'])
            for mecanico_id in request.POST.getlist('mecanicos'):
                trabajo_mecanico = Trabajo_mecanico(mecanico_id=mecanico_id, trabajo_id = trabajo.id)
                trabajo_mecanico.save()
            messages.add_message(request, messages.SUCCESS, 'Trabajo Guardado Exitosamente')
    else:
        formulario = TrabajoForm()
    return render(request, 'mecanica/trabajo_edit.html', {'formulario': formulario})

# def trabajo_edit(request, pk):
#     trabajo = get_object_or_404(Trabajo, pk=pk)
#     if request.method == "POST":
#         formulario = TrabajoForm(request.POST, instance=trabajo)
#         if formulario.is_valid():
#             trabajo = Trabajo.objects.create(auto_placas=formulario.cleaned_data['auto_placas'], trabajo_descripcion = formulario.cleaned_data['trabajo_descripcion'], costo_total = formulario.cleaned_data['costo_total'], estado = formulario.cleaned_data['estado'])
#             for mecanico_id in request.POST.getlist('mecanicos'):
#                 trabajo_mecanico = Trabajo_mecanico(mecanico_id=mecanico_id, trabajo_id = trabajo.id)
#                 trabajo_mecanico.save()
#             messages.add_message(request, messages.SUCCESS, 'Trabajo Actualizado Exitosamente')
#             return redirect('detalle_trabajo', pk=trabajo.pk)
#     else:
#         # formulario = TrabajoForm()
#         formulario = TrabajoForm(instance=trabajo)
#     return render(request, 'mecanica/trabajo_edit.html', {'formulario': formulario})

def trabajo_edit(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    if request.method == "POST":
        formulario = TrabajoForm(request.POST, instance=trabajo)
        if formulario.is_valid():
            trabajo = formulario.save(commit=False)
            trabajo.fecha_registro = timezone.now()
            trabajo.save()
            return redirect('detalle_trabajo', pk=trabajo.pk)
    else:
        formulario = TrabajoForm(instance=trabajo)
    return render(request, 'mecanica/trabajo_edit.html', {'formulario': formulario})

def trabajo_delete(request, pk):
    trabajo = Trabajo.objects.get(pk=pk)
    trabajo.delete()
    messages.add_message(request, messages.SUCCESS, 'Trabajo Borrado Exitosamente')
    # Después redireccionamos de nuevo a la lista
    return redirect('trabajo_list')