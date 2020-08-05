from django.db import models
from datetime import datetime
# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length = 100)
    last_name=models.CharField(max_length = 50)
    img=models.ImageField(upload_to='pics')
    specialty=models.CharField(max_length = 50)
    code=models.IntegerField()
    email=models.CharField(max_length = 25)
    password=models.CharField(max_length=10)
class Cite(models.Model):
    name=models.CharField(max_length = 100)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    area=models.CharField(max_length = 30)
    hora=models.TimeField()
    fecha=models.DateField()