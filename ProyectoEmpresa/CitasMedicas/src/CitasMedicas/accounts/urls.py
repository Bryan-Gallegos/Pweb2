from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('manage',views.manage,name='manage'),
    path('add',views.add,name='add'),
    path('otro_pdf',views.otro_pdf,name='otro_pdf'),
    path('show_doctors',views.show_doctors,name='show_doctors'),
    path('ver_contrato/<int:id>',views.ver_contrato,name='ver_contrato'),
    path('delete_page',views.delete_page,name='delete_page'),
    path('delete_obj/<int:id>',views.delete_obj,name='delete_obj'),
    path('modificate_obj/<int:id>',views.modificate_obj,name='modificate_obj'),
    path('make_appointment_page',views.make_appointment_page,name='make_appointment_page'),
    path('do_appointment/<str:area>',views.do_appointment,name='do_appointment'),
    #Doctor
    path('login_doctor',views.login_doctor,name='login_doctor'),
    #User
    path('ver_citas',views.ver_citas,name='ver_citas'),
    #Admin
    path('modificate_doctor/<int:id>',views.modificate_doctor,name='modificate_doctor'),
    path('manage_cites',views.manage_cites,name='manage_cites'),
    path('change_cites',views.change_cites,name='change_cites'),
    path('show_specialty_for_cites',views.show_specialty_for_cites,name='show_specialty_for_cites'),
    path('delete_cite/<int:id>',views.delete_cite,name='delete_cite'),
    path('modificate_cite/<int:id>',views.modificate_cite,name='modificate_cite'),
]