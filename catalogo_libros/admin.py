from django.contrib import admin
# Importa el modulo admin de Django para registrar los modelos en el panel de administracion

# importa los modelos que se van a registrar en el panel de administracion
from .models import Autor, Editora, Libros  # Importa los modelos

# admin.site.register(modelo) = Registra el modelo en el panel de administracion para que pueda ser gestionado a traves de la interfaz de admin
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Libros)
