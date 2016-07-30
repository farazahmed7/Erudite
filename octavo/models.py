from __future__ import unicode_literals
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



# Create your models here.

	
class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    def __str__(self):
		return self.name

    class MPTTMeta:
        order_insertion_by = ['name']	
		
class Search(models.Model):
	sem=models.TextField()
	def __str__(self):
		return self.sem
	
class Subject(MPTTModel):
	sub=models.CharField(max_length=50, unique=True)
	
	def __str__(self):
		return self.sub
	
		
	
