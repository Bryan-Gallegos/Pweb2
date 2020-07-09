from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Destination
from django.contrib.auth.models import User, auth
from .forms import PersonForm,RawDestinoForm
# Create your views here.
def index(request):

    dests=Destination.objects.all()

    return render(request,"index.html", {'dests': dests})

def add(request):
    form = RawPersonaForm()
def remove(request,myID):
    obj=get_object_or_404(Destination,id=myID)
    if request.method=='POST':
        messages.info(request,'Remove Destiny')
        obj.delete()
        return render('../')
    context ={
        'objeto':obj,
    }
    return render(request,'removeDestiny.html',context)
def edit(request):
    return render(request,'editDestiny.html')
def show(request,myID):
    obj=Destination.objects.get(id=myID)
    context ={
        'objeto':obj,
    }
    return render(request,'showDestiny.html',context)