from django.db import models

# Create your models here.
class CreaAlumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    
class CreaProfesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    
class CreaCurso(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):  
        return f"{self.nombre} {self.profesor} {self.descripcion}"