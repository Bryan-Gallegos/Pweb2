from django.urls import path
from . import views

urlpatterns=[
    path('add',views.add,name='add'),
    path('remove',views.remove,name='remove'),
    path('edit',views.edit,name='edit'),
    path('show/<int:myID>',views.show,name='show'),
]