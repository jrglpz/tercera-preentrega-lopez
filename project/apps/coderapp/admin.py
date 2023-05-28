from django.contrib import admin
from .models import CreaAlumno, CreaProfesor, CreaCurso
# Register your models here.
admin.site.register(CreaAlumno)
admin.site.register(CreaProfesor)
admin.site.register(CreaCurso)