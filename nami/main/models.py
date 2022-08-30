from django.db import models

# Create your models here.

class Namiwallet(models.Model):
	value= models.TextField()
	created= models.DateField(auto_now_add=True)
	
	def __str__(self):
		return self.value
