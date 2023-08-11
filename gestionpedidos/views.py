from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gestionpedidos.pedidos_form import PedidoForm

def index(request):
    return render(request, 'index.html')

def acta(request):
    return render(request, 'acta.html')

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.oficial = request.user  
            pedido.usuario_registro = request.user
            pedido.save()
            return redirect('crear_pedido')
    else:
        form = PedidoForm()

    context = {
        'form': form,
    }
    return render(request, 'pedidos.html', context)

def informes(request):
    return render(request, 'informes.html')

def oficiales(request):
    return render(request, 'informes.html')