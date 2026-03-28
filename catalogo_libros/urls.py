from catalogo_libros import views
from django.urls import path
# Se crea un archivo urls.py dentro de la app para definir las rutas especificas de la app,y luego se incluyen estas rutas en el archivo urls.py del proyecto

urlpatterns = [path("", views.listaLibros, name="lista_libros")]
