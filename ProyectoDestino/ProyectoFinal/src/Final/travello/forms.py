from django import forms 

class RawDestinoForm(forms.Form):
    name = forms.CharField(max_length=100)
    img = forms.ImageField(upload_to='pics')
    desc = forms.CharField()
    price = forms.IntegerField()
    offer = forms.BooleanField()