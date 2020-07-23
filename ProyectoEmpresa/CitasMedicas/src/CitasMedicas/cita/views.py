from django.shortcuts import render
from cita.models import Cite, Doctor
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    cits=Cite.objects.all()
    docs=Doctor.objects.all()
    return render(request,"index.html",{'docs':docs})
