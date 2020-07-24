from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addDestiny',views.addDestiny,name='addDestiny'),
    path("listar",views.listar,name="listar"),
    path('remove/<id>/',views.removeDestiny,name='removeDestiny'),
    path('edit/<id>/',views.editDestiny,name='editDestiny'),
]