from django.shortcuts import render
from .models import Salarios
from django.views.generic import TemplateView
from gestion_salarios.forms import SalariosForm
import gestion_salarios.models

# Create your views here.

class SalariosAdd(TemplateView):
    template_name = 'salarios/SalariosAgregar.html'

    def get(self, request, **kwargs):
        form = SalariosForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SalariosForm(request.POST)
        if form.is_valid():
            obj = gestion_salarios.models.Salarios.objects.all().first()
            obj.Contrato_colectivo = request.FILES['Contrato_colectivo']
            obj.save()

            return render(request, 'salarios/SalariosAgregar.html', {'form': form},)
        else:
            form = SalariosForm()
        return render(request,'salarios/SalariosAgregar.html', {'form': form})


class SalariosViewUpdate(TemplateView):
    template_name = 'salarios/SalariosVerEditar.html'


    def get(self, request, **kwargs):
        form = SalariosForm(request.POST)
        salarios = Salarios.objects.all().first()
        return render(request, self.template_name, {'form': form, 'salarios':salarios})

    def post(self, request):
        form = SalariosForm(request.POST)
        obj = Salarios.objects.all().first()
        if form.is_valid():

            obj.Contrato_colectivo = request.FILES['Contrato_colectivo']
            obj.save()
            return render(request, self.template_name)
        else:
            form = SalariosForm()
        return render(request, 'SalariosVerEditar.html', {'form': form})


class SalariosClean(TemplateView):
    template_name = 'salarios/SalariosLimpiar.html'

    def get(self, request, **kwargs):
        form = SalariosForm(request.POST)
        salarios = Salarios.objects.all().first()
        return render(request, self.template_name, {'form': form, 'salarios':salarios})

    def post(self, request):
        obj = Salarios.objects.all().first()

        obj.Contrato_colectivo.delete()
        obj.save()
        return render(request, self.template_name, {'obj': obj})

