from django.db import models


# class nombreEntidad(models.Model): activa el ORM (Object-Relational-Mapping) de Django para la clase que representa una entidad en la bd , lo que permite interactuar con la bd a traves de objetos de py en lugar de SQL
class Autor(models.Model):
    # atributo = models.TipoDeCampo(parametros) = Define un campo en el modelo, donde el tipo de campo determina el tipo de datos que se almacenaran en ese campo y los parametros configuran su comportamiento
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre}"


class Editora(models.Model):
    nombre_editora = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_editora}"


class Libros(models.Model):
    nombre_libro = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    # atributo = models.ForeignKey(EntidadRelacionada, on_delete=models.CASCADE, null= False) = Define una relacion de clave foranea entre el modelo actual y otro modelo, osea relaciona 2 tablas.
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, null=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    fecha_publicacion = models.DateField(null=False)
    imagen = models.ImageField(upload_to="media/", blank=True, null=True)
    sinopsis = models.TextField(null=False)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_libro}"
