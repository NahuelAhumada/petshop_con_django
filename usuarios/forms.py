from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuarios.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =  ["usuario", "nombre", "email","clave"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]