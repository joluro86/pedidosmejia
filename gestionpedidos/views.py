from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def acta(request):
    return render(request, 'acta.html')

def pedidos(request):
    return render(request, 'pedidos.html')

def informes(request):
    return render(request, 'informes.html')

def oficiales(request):
    return render(request, 'informes.html')