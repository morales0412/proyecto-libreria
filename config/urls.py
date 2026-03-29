from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "libros/",
        include("catalogo_libros.urls"),
    ),  # path("",include("app.urls")) = Incluye las urls definidas en el archivo urls.py de la app especificada
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # Agrega las rutas para servir archivos multimedia durante el desarrollo
# static() = Funcion que se usa para servirr archivos estaticos y multimedia durante el desarrollo (crea las rutas necesarias para acceder a estos archivos a traves de la url)
# settings.MEDIA_URL = Define la url base para acceder a los archivos multimedia, y document_root = settings.MEDIA_ROOT = Define la ruta en el sistema de archivos donde se almacenan los archivos multimedia.
