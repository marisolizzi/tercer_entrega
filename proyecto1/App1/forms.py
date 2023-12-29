from django import forms

class FormCurso(forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    numero = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Número','class':'form-control'}))
    detalle = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción','class':'form-control'}))
