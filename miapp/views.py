from django.shortcuts import render, HttpResponse, redirect

def cursos(request):
   return render(request,"cursos.html")
def crearcurso(request):
   return render(request,"crearcurso.html")
def carrera(request):
   return render(request,"carrera.html")
def crearcarrera(request):
   return render(request,"crearcarrera.html")
def index(request):
    return render(request,"index.html")