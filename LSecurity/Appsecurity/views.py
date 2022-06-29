from django.http import HttpResponse
from django.shortcuts import render
from Appsecurity.models import *
from Appsecurity.forms import *

# Create your views here.

def inicio(request):
    appsecurity = Alarmas.objects.all()
    contexto= {'alarmas':appsecurity} 
 
    return render(request,"Appsecurity/inicio.html",contexto)

def alarmas(request):

    appsecurity = Alarmas.objects.all()
    contexto= {'alarmas':appsecurity}

    return render(request,"Appsecurity/alarmas.html", contexto)        

def camaras(request):

    appsecurity = Camaras.objects.all()
    contexto= {'camaras':appsecurity}

    return render(request,"Appsecurity/camaras.html", contexto)       


def cerco(request):

    appsecurity = Cercos.objects.all()
    contexto= {'cerco':appsecurity}

    return render(request,"Appsecurity/cerco.html", contexto)           


def crearAlarma(request):

   if request.method == "POST":

        miFormulario = AlarmaFormulario(request.POST)

        print(miFormulario)

        if AlarmaFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           alarma = Alarmas (nombre=informacion['nombre'],foto=informacion['foto'], tipo=informacion['tipo'], precio=informacion['precio'])

           alarma.save()

           return render(request, "Appsecurity/inicio.html")    

   else:

      miFormulario = AlarmaFormulario()

   return render(request,'Appsecurity/formulario.html',{"miFormulario":miFormulario}) 

def crearCamara(request):

   if request.method == "POST":

        miFormulario = CamarasFormulario(request.POST)

        print(miFormulario)

        if CamarasFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           camaras = Camaras(nombre=informacion['nombre'],foto=informacion['foto'], definicion=informacion['definicion'], precio=informacion['precio'])

           camaras.save()

           return render(request, "Appsecurity/inicio.html")    

   else:

      miFormulario= CamarasFormulario()

   return render(request,'Appsecurity/formCamara.html',{"miFormulario":miFormulario})  

def crearCerco(request):

   if request.method == "POST":

        miFormulario = CercosFormulario(request.POST)

        print(miFormulario)

        if CercosFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           cerco = Cercos(nombre=informacion['nombre'],foto=informacion['foto'], voltaje=informacion['voltaje'], precio=informacion['precio'])

           cerco.save()

           return render(request, "Appsecurity/inicio.html")    

   else:

      miFormulario= CercosFormulario()

   return render(request,'Appsecurity/formCerco.html',{"miFormulario":miFormulario})        


def buscarAlarma(request):

    return render(request, "Appsecurity/buscarAlarma.html")

def buscar(request):

    if request.GET['nombre']:
       nombre = request.GET['nombre']
       alarmas = Alarmas.objects.filter(nombre__icontains=nombre)
       
       return render(request,"Appsecurity/resultadosBusqueda.html",{"alarmas": alarmas,"nombre":nombre})

    else:
      
      respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
