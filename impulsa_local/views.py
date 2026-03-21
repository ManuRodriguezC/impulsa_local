from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro_emprendedor(request):
    return render(request, 'registro-emprendedor.html')