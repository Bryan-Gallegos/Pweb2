import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect
from django.contrib import messages
from cita.models import Cite, Doctor
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from io import StringIO, BytesIO
from collections import OrderedDict
from datetime import date
from datetime import datetime

# Create your views here.

def pdf_cite(request):
    all_cites=Cite.objects.all()
    doctors=Doctor.objects.all()
    data={'cites':all_cites,'doctors':doctors}
    template=get_template("pdf_cites.html")
    data_p=template.render(data)
    response=BytesIO()
    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")


def ver_cita(request,id):
    select_cite=Cite.objects.get(id=id)
    data={'cite':select_cite}
    template=get_template("cite.html")
    data_p=template.render(data)
    response=BytesIO()
    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

def show_cites(request):
    cites=Cite.objects.all()
    return render(request,'show_cites.html',{'cites':cites})


def modificate_cite(request,id):
    if request.method=='POST':
        cite_mod=Cite.objects.get(id=id)
        cite_mod.name=request.POST['name']
        cite_mod.doctor_id=Doctor.objects.get(id=request.POST["select"])
        cite_mod.fecha=request.POST['date']
        cite_mod.hora=request.POST['time']
        cite_mod.email=request.POST['email']
        cite_mod.save()
        return redirect('/')
    hoy=datetime.now()
    print(str(hoy))
    cite=Cite.objects.get(id=id)
    doctors=Doctor.objects.all()
    print(str(cite.fecha))
    cadena=str(cite.fecha)
    fecha=datetime(2020,hoy.month,int(cadena[cadena.rfind("-")+1:len(cadena)]))
    cadena_hora=str(cite.hora)
    print(cadena_hora[:cadena_hora.find(":")])
    hora_cita=[cadena_hora[:cadena_hora.find(":")],cadena_hora[cadena_hora.find(":")+1:cadena_hora.rfind(":")]]
    hora=int(hora_cita[0])
    minuto=int(hora_cita[1])
    return render(request,'modificate_cite.html',{'cite':cite,'doctors':doctors,'hoy':hoy,'fecha':fecha,'hora':hora,'minuto':minuto})


def delete_cite(request,id):
    obj=Cite.objects.get(id=id)
    obj.delete()
    return redirect('/')


def change_cites(request):
    cites=Cite.objects.all()
    return render(request,'change_cites.html',{'cites':cites})

def show_specialty_for_cites(request):
    prueba=Doctor.objects.all()
    espec=[""+doc.specialty for doc in prueba]
    espec=list(OrderedDict.fromkeys(espec))
    return render(request,'specialty_page_for_cites.html',{'spec':espec})

def manage_cites(request):
    return render(request,'manage_cites.html',{})

def ver_citas(request):
    cites=[cite for cite in Cite.objects.all()]
    doctors=[doctor for doctor in Doctor.objects.all()]
    return render(request,'ver_citas.html',{'cites':cites,'doctors':doctors})

def login_doctor(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['password']
        doctor=Doctor.authenticate(email=email,password=name)
        print(doctor)
        if doctor:
            auth.login(request,doctor)
            subject="Iniciaste sesion en B&J"
            message="Acabas de iniciar sesion en B&J clinicas de la salud, Buen dia doctor"
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[doctor.email]
            send_mail(subject,message,email_from,recipient_list,)
            print("pase por aqui")
            return redirect('/')
    return render(request,'login_doctor.html',{})

def do_appointment(request,area):
    doctors=Doctor.objects.all()
    if request.method=='POST':
        #esta es la fecha actual
        fecha_actual=datetime.now()
        #datos
        print("paso por aca")
        name=request.POST['name']
        doctor_id=Doctor.objects.get(id=request.POST["select"])
        area_doctor=Doctor.objects.get(id=doctor_id.id)
        area_cita=area
        date_cita=request.POST['date']
        time=request.POST['time']
        email=request.POST['email']
        appointment=Cite.objects.create(name=name,doctor_id=doctor_id,area=area_cita,email=email,hora=time,fecha=date_cita)
        appointment.save()
        subject="Sacaste una cita en B&J Clinicas de la Salud"
        message="Acabas de sacar una cita para el dia "+date_cita+" en B&J Clinicas de la Salud\nPaciente: "+name+"\nEspecialidad: "+area_cita+"\nID del doctor: "+str(doctor_id.id)+"\nFecha: "+str(date_cita)+"Hora: "+time+"\nTE ESPERAMOS"
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[email]
        send_mail(subject,message,email_from,recipient_list,)
        return redirect('/')
    return render(request,"do_appointment.html",{'esp':area,'doctors':doctors})

def make_appointment_page(request):
    prueba=Doctor.objects.all()
    espec=[""+doc.specialty for doc in prueba]
    espec=list(OrderedDict.fromkeys(espec))
    return render(request,'specialty_page.html',{'spec':espec})

def modificate_obj(request,id):
    doc=Doctor.objects.get(id=id)
    return render(request,'modificate_obj.html',{'doc':doc})

def delete_obj(request,id):
    obj=Doctor.objects.get(id=id)
    obj.delete()
    return redirect('/')

def delete_page(request):
    doctors=Doctor.objects.all()
    return render(request,'delete_page.html',{'doctors':doctors})

def ver_contrato(request,id):
    select_doctor=Doctor.objects.get(id=id)
    data={'doctor':select_doctor}
    template=get_template("contrato.html")
    data_p=template.render(data)
    response=BytesIO()
    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

def show_doctors(request):
    doctors=Doctor.objects.all()
    return render(request,'show_doctors.html',{'doctors':doctors})

def otro_pdf(request):
    all_doctors=Doctor.objects.all()
    data={'doctors':all_doctors}
    template=get_template("pdf_page.html")
    data_p=template.render(data)
    response=BytesIO()
    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

def modificate_doctor(request,id):
    obj=Doctor.objects.get(id=id)
    print("Esta pasando por el metodo para modificar")
    if request.method=='POST':
        print("Entro al metodo para modificar")
        obj.name=request.POST['name']
        obj.last_name=request.POST['last_name']
        obj.img="pics/"+request.POST['img']
        obj.specialty=request.POST['especialty']
        obj.code=request.POST['code']
        obj.save()
        return render(request,'manage.html',{})
    return render(request,'manage.html',{})



def add(request):
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

"""def loginDoctor(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        usr=Doctor.objects.get(username=username,password=password)
        if user is not None:
            #ummm nose como combinarlo
            subject="Doctor inició sesión en B&J"
            message="Acaba de iniciar sesión en B&J clinicas de la salud, ven y mira cuales son sus citas programadas"
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[usr.email]
            send_mail(subject,message,email_from,recipient_list,)
            return redirect('/')
        else:
            messages.info(request,'Contraseña invalida')
            return redirect('login')
    else:
        return render(request,'login2.html')
    """
