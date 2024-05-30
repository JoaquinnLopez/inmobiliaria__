from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Terreno
from .forms import TerrenoForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def terrenos(request):
    terrenos = Terreno.objects.all()
    return render(request, 'terrenos/index.html', {'terrenos': terrenos})

def agregar(request):
    formulario = TerrenoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('terrenos')
    return render(request, 'terrenos/agregar.html', {'formulario': formulario})

def editar(request,id):
    terreno = Terreno.objects.get(id=id)
    formulario = TerrenoForm(request.POST or None, request.FILES or None, instance=terreno)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('terrenos')
    return render(request, 'terrenos/editar.html', {'formulario': formulario})

def borrar(request, id):
    terreno = Terreno.objects.get(id=id)
    terreno.delete()
    return redirect('terrenos')

