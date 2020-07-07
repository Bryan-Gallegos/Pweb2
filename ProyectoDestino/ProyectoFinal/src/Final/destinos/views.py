from django.shortcuts import render, redirect
from django.contrib import messages
from travello.models import Destination
from django.contrib.auth.models import User, auth
# Create your views here.
def add(request):
    if request.method=='POST':
        name=request.POST['name']
        img=request.post['image']
        desc=request.POST['desc']
        price=request.POST['price']
        offer=request.POST['offer']
    else:
        return render(request,'addDestiny.html')
def remove(request):
    return render(request,'removeDestiny.html')
def edit(request):
    return render(request,'editDestiny.html')
def show(request,myID):
    obj=Destination.objects.get(id=myID)
    context ={
        'objeto':obj,
    }
    return render(request,'showDestiny.html',context)