from django.shortcuts import render, get_object_or_404, redirect
from catalogo_libros.models import Libros
from catalogo_libros.forms import LibrosForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def lista_libros(request):
    libros = Libros.objects.all()  # variable = modelo.objects.all() = Consulta a la bd para obtener todos los registros de dicho modelo.
    return render(request, "catalogo/lista_libros.html", {"libros": libros})


def detalle_libro(request, id):
    # get_object_or_404(Modelo, id=id) = Consulta a la bd para obtener un registro específico del modelo basado en el id ,si no se encuentra el registro, devuelve un error 404.
    libro = get_object_or_404(Libros, id=id)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})


# decorador que protege la vista, requiere que el usuario este autenticado para acceder a ella, si no lo esta, redirige a la pagina de login
@login_required
def crear_libro(request):
    form = LibrosForm()
    # verifica si en el request se ha enviado un formulario(POST)
    if request.method == "POST":
        action = request.POST.get("action")
        # verifica si el usuario ha hecho clic en el botón de logout
        if action == "logout":
            logout(request)
            return redirect("login")
        # verifica si el usuario ha hecho clic en el botón de guardar
        elif action == "guardar":
            # crea una instancia del formulario con los datos enviados en el request
            # request.POST = datos del formulario, request.FILES = archivos enviados en el formulario (como imágenes)
            form = LibrosForm(request.POST, request.FILES)
            # confirma si el formulario es valido (cumple con las validaciones definidas en el formulario)
            if form.is_valid():
                # guarda los datos del formulario en la bd
                form.save()
                # muestra un mensaje de exito al usuario
                messages.success(request, "Libro creado correctamente")
                return redirect("crear_libro")
            else:
                # muestra un mensaje de error al usuario si el  form no es valido
                messages.error(request, "Error al crear el libro")
        else:
            # si el request no es POST, se crea una instancia vacia del formulario para mostrarlo al usuario
            form = LibrosForm()
        # vuelve a renderizar el formulario con los errores de validación pa que el usuario pueda corregirlas
    return render(request, "catalogo/crear_libro.html", {"form": form})


def login_view(request):
    # verifica si el request es POST, osea si el usuario ha enviado el form de login
    if request.method == "POST":
        # variable = request.POST.get("campo") = obtiene el valor del campo especificado en el form enviado por el usuario
        username = request.POST.get("username")
        password = request.POST.get("password")
        # verifica las credenciales y devuelve un objeto de usuario si son validas, o None si no lo son
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # inicia la sesión del usuario autenticado, permitiendo que acceda a las vistas protegidas por login_required
            login(request, user)
            return redirect("crear_libro")
        else:
            messages.error(request, "Usuario o contraseña invalidos")
    return render(request, "catalogo/login.html")


def logout_view(request):
    # logout(request) = cierra la sesión del usuario
    logout(request)
    return redirect("login")
