from django.shortcuts import render, redirect
from django.contrib import messages
from travello.models import Destination
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
                
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                
                return redirect('login')
        else:
            messages.info(request,'password not matching....')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def addDestiny(request):
    print('create image')
    if request.method=='POST':
        name=request.POST['name']
        direc=request.POST['direc']
        desc=request.POST['desc']
        price=request.POST['price']
        offer=request.POST.get['offer',False]
        if offer=='on':
            offer=True
        else:
            offer=False
        imgs=Destination.objects.create(name=name,img=direc,desc=desc,price=price,offer=offer)
        imgs.save()
        dests=Destination.objects.all()
    return render(request,'addDestiny.html')

def removeDestiny(request,id):
    data=Destination.objects.get(id=id)
    data.delete()
    return redirect(to='listar')

def editDestiny(request,id):
    data=Destination.objects.get(id=id)
    if request.method=='POST':
        data.id=request.POST['textid']
        data.name=request.POST['name']
        data.img=request.POST['direccion']
        data.desc=request.POST['desc']
        data.price=request.POST['price']
        data.offer=request.POST.get['offer',False]
        if data.offer=='on':
            data.offer=True
        else:
            data.offer=False
        data.save()
        return redirect('listar')
    return render(request,'editDestiny.html',{'data':data,})

def listar(request):
    data=Destination.objects.all()
    return render(request,'listar.html',{'data':data,})