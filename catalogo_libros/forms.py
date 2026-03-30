from .models import Libros
from django import forms


class LibrosForm(forms.ModelForm):
    # clase Meta = configuracion del formulario
    class Meta:
        # model = ModeloAsociado = especifica el modelo al que esta asociado el formulario
        model = Libros
        # fields = "__all__" = incluye todos los campos del modelo en el formulario
        fields = "__all__"
