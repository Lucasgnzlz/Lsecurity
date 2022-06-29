from django import forms


class AlarmasFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)
    tipo = forms.CharField(max_length=60) 
    precio = forms.IntegerField()   

class CamarasFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)     
    definicion = forms.CharField(max_length=50)
    precio = forms.IntegerField() 

class CercosFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)     
    voltaje = forms.CharField(max_length=50)
    precio = forms.IntegerField()   


