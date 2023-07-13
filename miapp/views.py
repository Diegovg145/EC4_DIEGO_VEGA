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
def crear_curso(request):
   curso = curso(
   titulo = "Tendencias Covid con Power BI",
   contenido = "El articulo muestra información de....",
   publicado = True
   )
   curso.save()
   return HttpResponse(f"curso Creado: {curso.titulo} - {curso.contenido}")