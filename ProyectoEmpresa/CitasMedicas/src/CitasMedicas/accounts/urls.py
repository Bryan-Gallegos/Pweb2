from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('manage',views.manage,name='manage'),
    path('add',views.add,name='add'),
    path('create_Pdf',views.create_Pdf,name='create_Pdf'),
    path('otro_pdf',views.otro_pdf,name='otro_pdf'),
    path('show_doctors',views.show_doctors,name='show_doctors'),
    path('ver_contrato/<int:id>',views.ver_contrato,name='ver_contrato'),
]