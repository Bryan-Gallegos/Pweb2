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
    print(prueba)
    espec=[""+doc.specialty for doc in prueba]
    espec=list(OrderedDict.fromkeys(espec))
    print(espec)
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
