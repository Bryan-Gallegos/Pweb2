from django.db import models
from datetime import datetime
# Create your models here.
class MedicalCite(models.Model):
    name=models.CharField(max_length=100)
    area=models.TextField()
    fecha=models.DateField()
    