from django.db import models
from datetime import datetime
# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length = 100)
    last_name=models.CharField(max_length = 150)
    specialty=models.CharField(max_length = 50)
    code=models.IntegerField()
class Cite(models.Model):
    name=models.CharField(max_length = 100)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    area=models.TextField()
    hora=models.TimeField()
    fecha=models.DateField()