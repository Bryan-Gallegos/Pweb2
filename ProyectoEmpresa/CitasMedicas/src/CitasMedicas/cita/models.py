from django.db import models
from datetime import datetime
# Create your models here.
class MedicalCite(models.Model):
    name=models.CharField(max_length=100)
    doctor=models.CharField(max_length=40)
    area=models.TextField()
    hora=models.TimeField()
    fecha=models.DateField()
    