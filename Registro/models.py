from django.db import models

# Create your models here.
class Usuario(models.Model):
    email=models.EmailField()