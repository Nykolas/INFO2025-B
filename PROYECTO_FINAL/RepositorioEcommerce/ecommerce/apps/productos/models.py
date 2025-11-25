from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length = 50)
	precio = models.DecimalField(max_digits = 8, decimal_places = 2)
	stock = models.IntegerField()
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to = 'productos')

	def __str__(self):
		return self.nombre

#generar y comprobar las migraciones
# py manage.py makemigrations

#para impactar los cambios en la BD
# py manage.py migrate
