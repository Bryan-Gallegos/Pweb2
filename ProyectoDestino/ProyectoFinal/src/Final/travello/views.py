from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name="Mumbai"
    dest1.img="destination_1.jpg"
    dest1.desc="la ciudad es interesasnte"
    dest1.price=700

    dest2=Destination()
    dest2.name="Destino 2"
    dest2.img="destination_2.jpg"
    dest2.desc="Este es el destino 2"
    dest2.price="870"

    dest3=Destination()
    dest3.name="Destino 3"
    dest3.img="destination_3.jpg"
    dest3.desc="Este es el destino 3"
    dest3.price="353"

    dests=[dest1,dest2,dest3]

    return render(request,"index.html", {'dests': dests})