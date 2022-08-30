from django.db import models

# Create your models here.

class Linea(models.Model):
    descripcion = models.CharField("Línea",max_length=100, unique=True)
    image = models.FileField(verbose_name = "Foto",upload_to="core/linea",blank=True,null=True)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name="Linea Producto"
        verbose_name_plural = "Lineas Productos"
        ordering=("id",)

    def __str__(self):
        return "{}".format(self.descripcion)

class Grupo(models.Model):
    linea= models.ManyToManyField(Linea)
    descripcion = models.CharField("Grupo",max_length=100, unique=True)
    image = models.FileField(verbose_name = "Foto",upload_to="core/grupo",blank=True,null=True)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name="Categoría"
        verbose_name_plural = "Categorías"
        ordering=("id",)

    def __str__(self):
        return "{}".format(self.descripcion)

#on_delete=models.CASCADE,null=True,blank=True)