from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.

def familiar(self):
    familiar1= Familiares(nombreyapellido= "Carlos Merlo", edad= 70, nacimiento= "1951-06-29")
    familiar1.save()
    familiar2= Familiares(nombreyapellido= "Alejandra Bach", edad= 61, nacimiento= "1961-02-16")
    familiar2.save()
    familiar3= Familiares(nombreyapellido= "Mariano Merlo", edad= 34, nacimiento= "1987-11-02")
    familiar3.save()
    
    texto= f"Familiar: {familiar1.nombreyapellido} Edad: {familiar1.edad} Nacimiento: {familiar1.nacimiento}"+"<br>"+f"Familiar: {familiar2.nombreyapellido} Edad: {familiar2.edad} Nacimiento: {familiar2.nacimiento}"+"<br>"+f"Familiar: {familiar3.nombreyapellido} Edad: {familiar3.edad} Nacimiento: {familiar3.nacimiento}"
    return HttpResponse(texto)

def indexhtml(self):
    miArchivo= open("C:/Users/Mariano.GONVAIO/Documents/MVT MARIANO MERLO/ProyectoBaseFamiliares/Plantillas/template1.html")
    plantilla= Template(miArchivo.read())
    miArchivo.close()
    contexto= Context()
    
    documento= plantilla.render(contexto)
    
    return HttpResponse(documento)