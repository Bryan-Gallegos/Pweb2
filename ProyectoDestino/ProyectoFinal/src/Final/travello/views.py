from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from travello.models import Destination
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request,"index.html", {'dests': dests})

