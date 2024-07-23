from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField

class ConsultaForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Consulta
        fields = [
            'nombre',
            'mensaje',
            'mail',
        ]
    def send_email(self, ):
        nombre = self.cleaned_data['nombre']
        mensaje= self.cleaned_data['mensaje']
        mail = self.cleaned_data['mail']

        #Logica de envio de mail