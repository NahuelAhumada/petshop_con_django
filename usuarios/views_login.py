from django.shortcuts import render

# Create your views here.
def pagina_login(request):
    params={}
    return render(request, "usuarios/login.html", params)
