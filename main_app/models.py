from django.db import models

# Create your models here.
class Treasure(models.Model):
	name = models.CharField(max_length=100)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	material = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	thelink = models.CharField(max_length=100)
	vimeo = models.CharField(max_length=100, default='http://www.vimeo.com')

	def __str__(self):
		return self.name
