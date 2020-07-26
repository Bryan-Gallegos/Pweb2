from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
<<<<<<< HEAD
    path('manage',views.manage,name='manage'),
    path('add',views.add,name='add'),
=======
>>>>>>> 36cb8f81cec0887c69b339e53e74e5be5fe53e90
]