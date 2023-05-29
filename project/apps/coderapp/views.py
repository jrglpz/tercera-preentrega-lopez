from django.shortcuts import render,redirect
from django.urls import reverse
from .form import CreaAlumnoForm, CreaProfesorForm, CreaCursoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def crearalumno(request):

    if request.method == "POST":
        form = CreaAlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("coderapp:index"))
    else:  
        form = CreaAlumnoForm()
    return render(request, "crearalumno.html", {"form": form})


def crearprofesor(request):

    if request.method == "POST":
        form = CreaProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("coderapp:index"))
    else:  
        form = CreaProfesorForm()
    return render(request, "crearprofesor.html", {"form": form})

def crearcurso(request):

    if request.method == "POST":
        form = CreaCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("coderapp:index"))
    else:  
        form = CreaCursoForm()
    return render(request, "crearcurso.html", {"form": form})
