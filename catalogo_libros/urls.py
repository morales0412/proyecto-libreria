from catalogo_libros import views
from django.urls import path
# Se crea un archivo urls.py dentro de la app para definir las rutas especificas de la app,y luego se incluyen estas rutas en el archivo urls.py del proyecto

urlpatterns = [
    path("", views.lista_libros, name="libros"),
    path("libro/<int:id>/", views.detalle_libro, name="detalle_libro"),
]
