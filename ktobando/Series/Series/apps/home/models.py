from django.db import models
from django.contrib.auth.models import User

class Idioma (models.Model):
	nombre		= models.CharField(max_length= 100)

	def __unicode__ (self):
		return self.nombre

class Editorial (models.Model):
	nombre		= models.CharField(max_length = 100)
	ciudad		= models.CharField(max_length = 100)
	stioweb		= models.URLField()

	def __unicode__ (self):
		return self.nombre

class Manga (models.Model):
	nombre				= models.CharField(max_length = 100)
	paginas				= models.DecimalField(max_digits= 6, decimal_places= 2)
	fecha_publicacion	= models.DateField()
	status				= models.BooleanField(max_length = True) 
	stock				= models.IntegerField()
	editorial 			= models.ForeignKey(Editorial)
	
	def __unicode__ (self):
		return self.nombre

class Marca (models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Marca/%s/%s"%(self.nombre, str(filename))
		return ruta

	nombre		= models.CharField(max_length = 100)
	material	= models.CharField(max_length = 100)
	imagen		= models.ImageField(upload_to= url, null = True,blank= True)

	def __unicode__ (self):
		return self.nombre

class Figuras (models.Model):
	nombre		= models.CharField(max_length = 100)
	serie		= models.CharField(max_length = 100)
	status		= models.BooleanField(max_length = True)
	stock		= models.IntegerField()
	marca 		= models.ForeignKey(Marca)
	def __unicode__ (self):
		return self.nombre
	
class Genero (models.Model):
	nombre		= models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 100)

	def __unicode__ (self):
		return self.nombre

class Series (models.Model):
	

	nombre		= models.CharField(max_length = 100)
	episodios	= models.DecimalField(max_digits= 6, decimal_places= 2)
	productor	= models.CharField(max_length = 100)
	genero		= models.CharField(max_length = 100)
	idioma		= models.ManyToManyField(Idioma, null= True, blank= True)
	manga		= models.CharField(max_length = 100)
	status		= models.BooleanField(default = True)
	figuras		= models.ForeignKey(Figuras)
	genero      = models.ManyToManyField(Genero, null= True, blank= True)
	stock		= models.IntegerField()

	def __unicode__ (self):
		return self.nombre


class user_profile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username.filename)
		return ruta

	user 		= models.OneToOneField(User)
	photo		= models.ImageField(upload_to=url)
	telefono	= models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username

