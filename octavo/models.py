from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Search(models.Model):
	sem=models.TextField()
	def __str__(self):
		return self.sem
	
class Subject(models.Model):
	sub=models.TextField()
	Search=models.ForeignKey(Search)
	def __str__(self):
		return self.sub	
	
	
