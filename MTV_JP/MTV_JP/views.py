from multiprocessing import context
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from AppFamilia.models import Familia

def saludo(hora_actual):

    hora_actual = datetime.now()
    contexto = {"dia": hora_actual}
    plantilla = loader.get_template('Template1.html')
    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def familia(self):
    familiar1 = Familia(nombre = 'Fernando', edad = 32, f_cumple = '1986-08-09')
    familiar1.save()
    documento1 = f"Se creó el familiar {familiar1.nombre} con edad {familiar1.edad} y fecha de nacimiento {familiar1.f_cumple}"

    familiar2 = Familia(nombre = 'Ana', edad = 2, f_cumple = '2020-10-09')
    familiar2.save()
    documento2 = f"Se creó el familiar {familiar2.nombre} con edad {familiar2.edad} y fecha de nacimiento {familiar2.f_cumple}"

    familiar3 = Familia(nombre = 'Jocelyne', edad = 10, f_cumple = '2012-08-09')
    familiar3.save()
    documento3 = f"Se creó el familiar {familiar3.nombre} con edad {familiar3.edad} y fecha de nacimiento {familiar3.f_cumple}"

    return HttpResponse(documento1)
