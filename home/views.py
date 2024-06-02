from django.shortcuts import render

# Create your views here.
def index(request):
    params = {}
    params['nombre_sitio']='Vida Silvestre'
    return render(request, 'home/index.html', params)