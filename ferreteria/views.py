from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuarios, TiposNovedades, Novedades, Usuarios_Novedades
from .forms import UsuariosForm, TiposNovedadesForm, NovedadesForm, UsuariosNovedadesForm, UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# ... otras importaciones y código ...

def front(request):
    # Puedes agregar lógica específica si es necesario
    return render(request, 'inicio/front.html')
#USUARIOS

def index_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/index_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_usuarios')
    else:
        form = UsuariosForm()
    return render(request, 'usuarios/crear.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index_usuarios')
    else:
        form = UsuariosForm(instance=usuario)
    return render(request, 'usuarios/editar.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('index_usuarios')
    return render(request, 'usuarios/eliminar.html', {'usuarios': Usuarios})

#TIPOSNOVEDADES

def index_tipos_novedades(request):
    tipos_novedades = TiposNovedades.objects.all()
    return render(request, 'tiposNovedades/index_tiposNovedades.html', {'tipos_novedades': tipos_novedades})

def crear_tipo_novedad(request):
    if request.method == 'POST':
        form = TiposNovedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_tipo_novedad')
    else:
        form = TiposNovedadesForm()
    return render(request, 'tiposNovedades/crear.html', {'form': form})

def editar_tipo_novedad(request, pk):
    tipo_novedad = get_object_or_404(TiposNovedades, pk=pk)
    if request.method == 'POST':
        form = TiposNovedadesForm(request.POST, instance=tipo_novedad)
        if form.is_valid():
            form.save()
            return redirect('index_tipos_novedades')
    else:
        form = TiposNovedadesForm(instance=tipo_novedad)
    return render(request, 'tiposNovedades/editar.html', {'form': form, 'tipo_novedad': tipo_novedad})

def eliminar_tipo_novedad(request, pk):
    tipo_novedad = get_object_or_404(TiposNovedades, pk=pk)
    if request.method == 'POST':
        tipo_novedad.delete()
        return redirect('index_tipos_novedades')
    return render(request, 'tiposNovedades/eliminar.html', {'tipo_novedad': tipo_novedad})
#NOVEDADES

def index_novedades(request):
    novedades = Novedades.objects.all()
    return render(request, 'novedades/index_novedades.html', {'novedades': novedades})

def crear_novedad(request):
    if request.method == 'POST':
        form = NovedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_usuarios_novedad')
    else:
        form = NovedadesForm()
    return render(request, 'novedades/crear.html', {'form': form})

def editar_novedad(request, pk):
    novedad = get_object_or_404(Novedades, pk=pk)
    if request.method == 'POST':
        form = NovedadesForm(request.POST, instance=novedad)
        if form.is_valid():
            form.save()
            return redirect('index_novedades')
    else:
        form = NovedadesForm(instance=novedad)
    return render(request, 'novedades/editar.html', {'form': form, 'novedad': novedad})

def eliminar_novedad(request, pk):
    novedad = get_object_or_404(Novedades, pk=pk)
    if request.method == 'POST':
        novedad.delete()
        return redirect('index_novedades')
    return render(request, 'novedades/eliminar.html', {'novedad': novedad})
#USUARIOSNOVEDADES

def index_usuarios_novedades(request):
    usuarios_novedades = Usuarios_Novedades.objects.all()
    return render(request, 'usuarios_novedades/index_usuarios_novedades.html', {'usuarios_novedades': usuarios_novedades})

def crear_usuarios_novedad(request):
    if request.method == 'POST':
        form = UsuariosNovedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_usuarios_novedades')
    else:
        form = UsuariosNovedadesForm()
    return render(request, 'usuarios_novedades/crear.html', {'form': form})

def editar_usuarios_novedad(request, pk):
    usuario_novedad = get_object_or_404(Usuarios_Novedades, pk=pk)
    if request.method == 'POST':
        form = UsuariosNovedadesForm(request.POST, instance=usuario_novedad)
        if form.is_valid():
            form.save()
            return redirect('index_usuarios_novedades')
    else:
        form = UsuariosNovedadesForm(instance=usuario_novedad)
    return render(request, 'usuarios_novedades/editar.html', {'form': form, 'usuario_novedad': usuario_novedad})

def eliminar_usuarios_novedad(request, pk):
    usuario_novedad = get_object_or_404(Usuarios_Novedades, pk=pk)
    if request.method == 'POST':
        usuario_novedad.delete()
        return redirect('index_usuarios_novedades')
    return render(request, 'usuarios_novedades/eliminar.html', {'usuario_novedad': usuario_novedad})

# LOGIN

def welcome(request):
    return render(request, 'login/welcome.html')

# REGISTRARSE

def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                return redirect('signin')
            except IntegrityError:
                return render(request, 'login/signup.html', {"form": UserCreationForm, "error": "El nombre de usuario ya existe."})

        return render(request, 'login/signup.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})

# INICIAR SESION

def signin(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html', {"formAuth": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/signin.html', {"formAuth": AuthenticationForm, "error": "Usuario o contraseña incorrecta."})

        login(request, user)
        return redirect('front')
    
# CERRAR SESION

def signout(request):
    logout(request)
    return redirect('welcome')
