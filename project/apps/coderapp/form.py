from django import forms
from .models import CreaAlumno, CreaProfesor, CreaCurso

class CreaAlumnoForm(forms.ModelForm):
    class Meta:
        model = CreaAlumno
        fields = ['nombre', 'apellido', 'email']

class CreaProfesorForm(forms.ModelForm):
    class Meta:
        model = CreaProfesor
        fields = ['nombre', 'apellido', 'email']

class CreaCursoForm(forms.ModelForm):
    class Meta:
        model = CreaCurso
        fields = ['nombre', 'profesor', 'descripcion']