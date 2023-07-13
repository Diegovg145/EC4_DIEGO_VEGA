from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    hstateour = models.IntegerField()
    cre = models.CharField(max_length=255)
    its = models.IntegerField() 
# auto_now_add me permitirá registrar
# la fecha cuando cree el registro
creado = models.DateTimeField(auto_now_add=True)
# auto_now me permitirá registrar
# la fecha cuando se modifique el registro
actualizado = models.DateTimeField(auto_now=True)
class Categoria(models.Model):
    cursos = models.CharField(max_length=100)
descripcion = models.CharField(max_length=250)
# DateField() para guardar la fecha manualmente
creado = models.DateField()
