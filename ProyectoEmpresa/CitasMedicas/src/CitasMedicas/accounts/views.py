from django.shortcuts import render, redirect
from django.contrib import messages
from cita.models import Cite, Doctor
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def modificate(request):
    return 3

def add(request):
    print('crear imagen')
    if request.method=='POST':
        print('creando doctor')
        Name=request.POST['name']
        Last_name=request.POST['last_name']
        Foto="pics/"+request.POST['img']
        Esp=request.POST['especialty']
        Cod=request.POST['code']
        print(Name)
        print(Last_name)
        print(Esp)
        imgs=Doctor.objects.create(name=Name,last_name=Last_name,img=Foto,specialty=Esp,code=Cod)
        imgs.save()
        print('doctor agregado')
        docs=Doctor.objects.all()
    return render(request,'add.html',{})

def manage(request):
    return render(request,'manage.html',{})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            subject="Iniciaste sesion en B&J"
            message="Acabas de iniciar sesion en B&J clinicas de la salud, ven y separa tu cita en la especialidad que desees"
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[user.email]
            send_mail(subject,message,email_from,recipient_list,)
            return redirect('/')
        else:
            messages.info(request,'Contraseña invalida')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username ya existente')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email ya existente')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                subject="Registro Completo"
                message="Felicidades "+user.first_name+", acabas de registrarte en B&J Clinicas de la Salud, saca una cita ahora y obten hasta un 70% de descuento en tu proxima consulta, ven y conoce nuestras nuevas especialidades"
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[user.email]
                send_mail(subject,message,email_from,recipient_list,)
                return redirect('login')
        else:
            messages.info(request,'Contraseña invalida')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
    return render(request,'about.html')