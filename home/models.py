from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.CharField(max_length=200)
	Phone=models.CharField(max_length=200)
	desc=models.TextField()
	date=models.DateField()