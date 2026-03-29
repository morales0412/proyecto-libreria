from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo_libros", "0002_rename_nombre_editora_nombre_editora"),
    ]

    operations = [
        migrations.RenameField(
            model_name="libros",
            old_name="nombre_libro",
            new_name="nombreLibro",
        ),
        migrations.RenameField(
            model_name="libros",
            old_name="fecha_publicacion",
            new_name="fechaPublicacion",
        ),
    ]
