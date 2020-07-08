from django.shortcuts import render, get_object_or_404, redirect
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
def remove(request,myID):
    obj=get_object_or_404(Destination,id=myID)
    if request.method=='POST':
        messages.info(request,'Remove Destiny')
        obj.delete()
        return render(request,'index.html')
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