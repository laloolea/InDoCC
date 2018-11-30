from django.shortcuts import render
from .models import Promocion
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def promocion(request):
    p = Promocion.objects.get(pk=2)

    return render(request, 'promocion/detail.html',{"promocion":p})


def promocion_form(request):
    p = Promocion.objects.get(pk=2)
    if request.method == "POST":

        if request.POST["SiNo"] == "true":
            p.Hay_proceso_promocion = True
        else:
            p.Hay_proceso_promocion = False

        if request.POST["SiNo2"] == "true":
            p.Hay_reglamento_proceso = True
        else:
            p.Hay_reglamento_proceso = False

        p.Descripcion = request.POST["texto"]

        if request.POST["SiNo3"] == "true":
            p.Hay_difusion_proceso = True
        else:
            p.Hay_difusion_proceso = False

        p.DescripcionDifusion = request.POST["texto2"]

        p.save()

        return HttpResponseRedirect(reverse('home:index'))

    return render(request, 'promocion/promocion.html',{"promocion":p})

