from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.
def pagina_logout(request):
    params={}
    logout(request)
    return render(request, "usuarios/logout.html", params)