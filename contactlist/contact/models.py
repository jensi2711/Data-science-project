from django.db import models
from django.forms import ModelForm

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contact=models.BigIntegerField()
class contactform(ModelForm):
    model=contact
    fields=["name","email","password","contact"]

