from django import forms

class FormBuscador(forms.Form):
    nombre_curso = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Nombre del Curso','class':'form-control','style':'width:350px;'}))

class FormCurso(forms.Form):
    nombre = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    numero = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Número','class':'form-control'}))
    detalle = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción','class':'form-control'}))

class FormEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    apellido = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Apellido','class':'form-control'}))
    email = forms.EmailField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))

class FormProfesor(forms.Form):
    nombre = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    apellido = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Apellido','class':'form-control'}))
    email = forms.EmailField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    profesion = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Profesión','class':'form-control'}))

class FormEntregable(forms.Form):
    nombre = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    fechaDeEntrega = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control','style':'margin-bottom:10px;'}))
    entregado = forms.BooleanField(required=False)
    detalle = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Observaciones','class':'form-control'}))
