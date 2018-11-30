from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.urls import reverse
from django.db import IntegrityError

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required
@user_passes_test(is_admin)
def index(request):
    if request.method == "POST":
        try:
            docente = User.objects.get(username=request.POST['user_to_delete'])
            docente.delete()
        except:
            pass
        

    docentes = User.objects.filter(groups__name='Docente')
    if docentes.count() > 0:
        return render(request, 'gestion_docentes/index.html', {"docentes":docentes})
    else:
        return render(request, 'gestion_docentes/index.html')

@login_required
@user_passes_test(is_admin)
def registro(request):
    if request.method == 'POST':
        docente = User(
            username=request.POST['username'],
            password="",
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )

        try:
            docente.set_password(request.POST['password'])
            docente.save()
            docente.groups.add(Group.objects.get(name='Docente'))
        except IntegrityError:
            error = "Nombre de usuario ya registrado"
            return render(request, 'gestion_docentes/docente_form.html', {"error_message":error})
        return HttpResponseRedirect(reverse('gestion_docentes:index'))
    else:
        return render(request, 'gestion_docentes/docente_form.html')

@login_required
@user_passes_test(is_admin)
def detail(request, user):
    if request.method == 'POST':
        docente = User.objects.get(username=user)
        docente.username = request.POST['username']
        docente.set_password(request.POST['password'])
        docente.first_name = request.POST['first_name']
        docente.last_name = request.POST['last_name']
        try:
            docente.save()
        except:
            return render(request, 'gestion_docentes/detail.html',
                {
                    "register_error":"El nombre de usuario que intentas guardar le pertenece a otro usuario.",
                    "docente":docente
                })
        return HttpResponseRedirect(reverse('gestion_docentes:index'))
    else:
        try:
            docente = User.objects.get(username=user)
            if docente.groups.filter(name='Admin').exists():
                raise Exception()
            return render(request, 'gestion_docentes/detail.html', {"docente":docente})
        except:
            return render(request, 'gestion_docentes/detail.html', {"url_error":"El usuario que buscas no existe."})
