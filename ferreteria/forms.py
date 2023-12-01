from django import forms
from .models import Usuarios, TiposNovedades, Novedades, Usuarios_Novedades
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsuariosForm(forms.ModelForm):
    nombres = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    apellidos = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={'invalid': 'Ingrese un correo electrónico válido.'}
    )

    celular = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
    )

    class Meta:
        model = Usuarios
        fields = ['nombres', 
                  'apellidos', 
                  'email', 
                  'celular', 
                  'fecha_nacimiento']

class TiposNovedadesForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = TiposNovedades
        fields = '__all__'

class NovedadesForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
    )

    fecha_finalizacion = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
    )

    dias_acumulados = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    tipoNovedad = forms.ModelChoiceField(
        queryset=TiposNovedades.objects.all().order_by('nombre'),
        empty_label="Seleccione tipo de novedad...",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    descripcion = forms.CharField(
        max_length=155,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'3'})
    )

    class Meta:
        model = Novedades
        fields = '__all__'

class UsuariosNovedadesForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.all().order_by('apellidos'),
        empty_label="Seleccione Usuario...",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    novedad = forms.ModelChoiceField(
        queryset=Novedades.objects.all(),
        empty_label="Seleccione Novedad...",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    class Meta:
        model = Usuarios_Novedades
        fields = '__all__'

class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Repita Contraseña'})
    )


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']
