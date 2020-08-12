from rest_framework import serializers
from cita.models import Cite, Doctor
class Doctor_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('id','name','last_name','img','specialty','code','email','password')

class Cite_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Cite
        fields=('id','name','doctor_id','area','hora','fecha')