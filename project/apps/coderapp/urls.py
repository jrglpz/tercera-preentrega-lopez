from django.contrib import admin
from django.urls import path, include
from .views import index, crearalumno, crearprofesor, crearcurso

app_name = "coderapp"

urlpatterns = [
    path("", index, name="index"),
    path("crearalumno/", crearalumno, name="crearalumno"),
    path("crearprofesor/", crearprofesor, name="crearprofesor"),
    path("crearcurso/", crearcurso, name="crearcurso"),
]