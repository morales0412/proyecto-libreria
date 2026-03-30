from .models import Libros
from django import forms
from datetime import datetime


class LibrosForm(forms.ModelForm):
    # clase Meta = configuracion del formulario
    class Meta:
        # model = ModeloAsociado = especifica el modelo al que esta asociado el formulario
        model = Libros
        # fields = "__all__" = incluye todos los campos del modelo en el formulario
        fields = "__all__"

        widgets = {
            # especificamos el widget para el campo fechaPublicacion, indicando que es un input de tipo date
            "fechaPublicacion": forms.DateInput(attrs={"type": "date"}),
        }
        # help_texts = {} = diccionario que permite agregar texto de ayuda para cada campo del formulario
        help_texts = {"fechaPublicacion": "Ingresa la fecha en el formato día/mes/año"}

    def clean_fechaPublicacion(self):
        fecha = self.cleaned_data.get("fechaPublicacion")
        if not fecha:
            return None

        # Si ya es un objeto date, lo devolvemos tal cual
        if isinstance(fecha, datetime):
            return fecha.date()

        # Intentamos parsear la fecha manualmente
        formatos = [
            "%Y-%m-%d",  # 2024-02-13
            "%d/%m/%Y",  # 13/02/2024
            "%d-%m-%Y",  # 13-02-2024
            "%m/%d/%Y",  # 02/13/2024
            "%m-%d-%Y",  # 02-13-2024
        ]
        for fmt in formatos:
            try:
                return datetime.strptime(str(fecha), fmt).date()
            except ValueError:
                continue

        raise forms.ValidationError(
            "Formato de fecha no reconocido. Usa algo como 2024-02-13 o 13/02/2024."
        )
