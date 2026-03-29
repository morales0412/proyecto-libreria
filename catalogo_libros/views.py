from django.shortcuts import render, get_object_or_404
from catalogo_libros.models import Libros


def lista_libros(request):
    libros = Libros.objects.all()  # variable = modelo.objects.all() = Consulta a la bd para obtener todos los registros de dicho modelo.
    return render(request, "catalogo/lista_libros.html", {"libros": libros})


def detalle_libro(request, id):
    # get_object_or_404(Modelo, id=id) = Consulta a la bd para obtener un registro específico del modelo basado en el id ,si no se encuentra el registro, devuelve un error 404.
    libro = get_object_or_404(Libros, id=id)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})
