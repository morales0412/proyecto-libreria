from django.shortcuts import render
from catalogo_libros.models import Libros


def listaLibros(request):
    libros = Libros.objects.all()  # variable = modelo.objects.all() = Consulta a la bd para obtener todos los registros de dicho modelo.
    return render(request, "catalogo/lista_libros.html", {"libros": libros})
