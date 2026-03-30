from django.shortcuts import render, get_object_or_404, redirect
from catalogo_libros.models import Libros
from catalogo_libros.forms import LibrosForm
from django.contrib import messages


def lista_libros(request):
    libros = Libros.objects.all()  # variable = modelo.objects.all() = Consulta a la bd para obtener todos los registros de dicho modelo.
    return render(request, "catalogo/lista_libros.html", {"libros": libros})


def detalle_libro(request, id):
    # get_object_or_404(Modelo, id=id) = Consulta a la bd para obtener un registro específico del modelo basado en el id ,si no se encuentra el registro, devuelve un error 404.
    libro = get_object_or_404(Libros, id=id)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})


def crear_libro(request):
    # verifica si en el request se ha enviado un formulario(POST)
    if request.method == "POST":
        # crea una instancia del formulario con los datos enviados en el request
        # request.POST = datos del formulario, request.FILES = archivos enviados en el formulario (como imágenes)
        form = LibrosForm(request.POST, request.FILES)
        # confirma si el formulario es valido (cumple con las validaciones definidas en el formulario)
        if form.is_valid():
            # guarda los datos del formulario en la bd
            form.save()
            # muestra un mensaje de exito al usuario
            messages.success(request, "Libro creado correctamente")
            return redirect("libros")
        else:
            # muestra un mensaje de error al usuario si el  form no es valido
            messages.error(request, "Error al crear el libro")
    else:
        # si el request no es POST, se crea una instancia vacia del formulario para mostrarlo al usuario
        form = LibrosForm()
    # vuelve a renderizar el formulario con los errores de validación pa que el usuario pueda corregirlas
    return render(request, "catalogo/crear_libro.html", {"form": form})
