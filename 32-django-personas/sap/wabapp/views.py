from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Domicilio, Persona

# Create your views here.


def bienvenido(request):
    no_personas_var = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas})


def indexDomicilio(request):
    no_domicilio_var = Domicilio.objects.count()
    # domicilios = Domicilio.objects.all()
    domicilios = Domicilio.objects.order_by('id')
    return render(request, 'indexDomicilio.html', {'no_domicilio': no_domicilio_var, 'domicilios': domicilios})
