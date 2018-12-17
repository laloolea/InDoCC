from django.shortcuts import render
from .models import Promocion
from django.views.generic import TemplateView
from gestion_promocion.forms import PromocionForm
import gestion_promocion.models

# Create your views here.

class PromocionAdd(TemplateView):
    template_name = 'promocion/PromocionAgregar.html'

    def get(self, request, **kwargs):
        form = PromocionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PromocionForm(request.POST)
        if form.is_valid():
            obj = gestion_promocion.models.Promocion.objects.all().first()
            obj.Hay_proceso_promocion = form.cleaned_data['Hay_proceso_promocion']
            obj.Hay_reglamento_proceso = form.cleaned_data['Hay_reglamento_proceso']
            obj.Descripcion = form.cleaned_data['Descripcion']
            obj.Hay_difusion_proceso = form.cleaned_data['Hay_difusion_proceso']
            obj.DescripcionDifusion = form.cleaned_data['DescripcionDifusion']
            obj.Evidencia = request.FILES.get('Evidencia', False)
            obj.save()

            return render(request, 'promocion/PromocionAgregar.html', {'form': form},)
        else:
            form = PromocionForm()
        return render(request,'promocion/PromocionAgregar.html', {'form': form})


class PromocionViewUpdate(TemplateView):
    template_name = 'promocion/PromocionVerEditar.html'


    def get(self, request, **kwargs):
        form = PromocionForm(request.POST)
        promocion = Promocion.objects.all().first()
        return render(request, self.template_name, {'form': form, 'promocion':promocion})

    def post(self, request):
        form = PromocionForm(request.POST)
        obj = Promocion.objects.all().first()
        if form.is_valid():
            obj.Hay_proceso_promocion = form.cleaned_data['Hay_proceso_promocion']
            obj.Hay_reglamento_proceso = form.cleaned_data['Hay_reglamento_proceso']
            obj.Descripcion = form.cleaned_data['Descripcion']
            obj.Hay_difusion_proceso = form.cleaned_data['Hay_difusion_proceso']
            obj.DescripcionDifusion = form.cleaned_data['DescripcionDifusion']
            obj.Evidencia = request.FILES.get('Evidencia', False)
            obj.save()
            return render(request, self.template_name)
        else:
            form = PromocionForm()
        return render(request, 'PromocionVerEditar.html', {'form': form})


class PromocionClean(TemplateView):
    template_name = 'Promocion/PromocionLimpiar.html'

    def get(self, request, **kwargs):
        form = PromocionForm(request.POST)
        promocion = Promocion.objects.all().first()
        return render(request, self.template_name, {'form': form, 'promocion':promocion})

    def post(self, request):
        obj = Promocion.objects.all().first()
        obj.Hay_proceso_promocion = False
        obj.Hay_reglamento_proceso = False
        obj.Descripcion = ' '
        obj.Hay_difusion_proceso = False
        obj.DescripcionDifusion = ' '
        obj.Evidencia.delete()
        obj.save()
        return render(request, self.template_name, {'obj': obj})
        #return render(request, 'PromocionAgregar.html', {'form': form})
