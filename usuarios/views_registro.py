from django.shortcuts import render

# Create your views here.
def pagina_registro(request):
    params={}
    return render(request, "usuarios/registro.html", params)