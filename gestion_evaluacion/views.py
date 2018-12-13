from django.shortcuts import render
from gestion_evaluacion.models import Evaluacion
from django.views.generic import TemplateView
from gestion_evaluacion.forms import EvaluacionForm


# Create your views here.

class EvaluacionAdd(TemplateView):
    template_name = 'evaluacion/EvaluacionAgregar.html'

    def get(self, request, **kwargs):
        form = EvaluacionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            obj = Evaluacion.objects.all().first()
            obj.Hay_evaluacion_estudiantes = form.cleaned_data['Hay_evaluacion_estudiantes']
            obj.Descripcion_evaluacion_estudiantes = form.cleaned_data['Descripcion_evaluacion_estudiantes']
            obj.Hay_mecanismos_evaluacion = form.cleaned_data['Hay_mecanismos_evaluacion']
            obj.Esta_reglamentado_mecanismos = form.cleaned_data['Esta_reglamentado_mecanismos']
            obj.Descripcion_mecanismos = form.cleaned_data['Descripcion_mecanismos']
            obj.Grupo_colegiado = form.cleaned_data['Grupo_colegiado']
            obj.Descripcion_gruposColegiados = form.cleaned_data['Descripcion_gruposColegiados']
            obj.Evidencia_grupoColegiados = request.FILES['Evidencia_grupoColegiados']
            obj.Estudiantes = form.cleaned_data['Estudiantes']
            obj.Descripcion_estudiantes = form.cleaned_data['Descripcion_estudiantes']
            obj.Evidencia_estudiante = request.FILES['Evidencia_estudiante']
            obj.Otras_instancias = form.cleaned_data['Otras_instancias']
            obj.Descripcion_instancias = form.cleaned_data['Descripcion_instancias']
            obj.Evidencia_instancias = request.FILES['Evidencia_instancias']
            obj.Hay_difusion = form.cleaned_data['Hay_difusion']
            obj.Tipo_difusion = form.cleaned_data['Tipo_difusion']
            obj.Resultados_periodos = request.FILES['Resultados_periodos']
            obj.Descripcion_entrega = form.cleaned_data['Descripcion_entrega']
            obj.Hay_criterios = form.cleaned_data['Hay_criterios']
            obj.Criterios_principales = form.cleaned_data['Criterios_principales']
            obj.Hay_programa_estimulos = form.cleaned_data['Hay_programa_estimulos']
            obj.DescripcionDifusion = form.cleaned_data['DescripcionDifusion']

            obj.save()
            return render(request, 'evaluacion/EvaluacionAgregar.html', {'form': form}, )
        else:
            form = EvaluacionForm()
        return render(request, 'EvaluacionAgregar.html', {'form': form})


class EvaluacionViewUpdate(TemplateView):
    template_name = 'evaluacion/EvaluacionVerEditar.html'


    def get(self, request, **kwargs):
        form = EvaluacionForm(request.POST)
        evaluacion = Evaluacion.objects.all().first()
        return render(request, self.template_name, {'form': form, 'evaluacion':evaluacion})

    def post(self, request):
        form = EvaluacionForm(request.POST)
        obj = Evaluacion.objects.all().first()
        if form.is_valid():
            obj = Evaluacion.objects.all().first()
            obj.Hay_evaluacion_estudiantes = form.cleaned_data['Hay_evaluacion_estudiantes']
            obj.Descripcion_evaluacion_estudiantes = form.cleaned_data['Descripcion_evaluacion_estudiantes']
            obj.Hay_mecanismos_evaluacion = form.cleaned_data['Hay_mecanismos_evaluacion']
            obj.Esta_reglamentado_mecanismos = form.cleaned_data['Esta_reglamentado_mecanismos']
            obj.Descripcion_mecanismos = form.cleaned_data['Descripcion_mecanismos']
            obj.Grupo_colegiado = form.cleaned_data['Grupo_colegiado']
            obj.Descripcion_gruposColegiados = form.cleaned_data['Descripcion_gruposColegiados']
            obj.Evidencia_grupoColegiados = request.FILES['Evidencia_grupoColegiados']
            obj.Estudiantes = form.cleaned_data['Estudiantes']
            obj.Descripcion_estudiantes = form.cleaned_data['Descripcion_estudiantes']
            obj.Evidencia_estudiante = request.FILES['Evidencia_estudiante']
            obj.Otras_instancias = form.cleaned_data['Otras_instancias']
            obj.Descripcion_instancias = form.cleaned_data['Descripcion_instancias']
            obj.Evidencia_instancias = request.FILES['Evidencia_instancias']
            obj.Hay_difusion = form.cleaned_data['Hay_difusion']
            obj.Tipo_difusion = form.cleaned_data['Tipo_difusion']
            obj.Resultados_periodos = request.FILES['Resultados_periodos']
            obj.Descripcion_entrega = form.cleaned_data['Descripcion_entrega']
            obj.Hay_criterios = form.cleaned_data['Hay_criterios']
            obj.Criterios_principales = form.cleaned_data['Criterios_principales']
            obj.Hay_programa_estimulos = form.cleaned_data['Hay_programa_estimulos']
            obj.DescripcionDifusion = form.cleaned_data['DescripcionDifusion']

            obj.save()
            return render(request, self.template_name)
        else:
            form = Evaluacion()
        return render(request, 'EvaluacionVerEditar.html', {'form': form})

class EvaluacionClean(TemplateView):
    template_name = 'Evaluacion/EvaluacionLimpiar.html'

    def get(self, request, **kwargs):
        form = EvaluacionForm(request.POST)
        evaluacion = Evaluacion.objects.all().first()
        return render(request, self.template_name, {'form': form, 'evaluacion': evaluacion})

    def post(self, request):


        obj = Evaluacion.objects.all().first()
        obj.Hay_evaluacion_estudiantes = False
        obj.Descripcion_evaluacion_estudiantes = ' '
        obj.Hay_mecanismos_evaluacion = False
        obj.Esta_reglamentado_mecanismos = False
        obj.Descripcion_mecanismos = ' '
        obj.Grupo_colegiado = False
        obj.Descripcion_gruposColegiados = ' '
        obj.Evidencia_grupoColegiados.delete()
        obj.Estudiantes = False
        obj.Descripcion_estudiantes = ' '
        obj.Evidencia_estudiante.delete()
        obj.Otras_instancias = False
        obj.Descripcion_instancias = ' '
        obj.Evidencia_instancias.delete()
        obj.Hay_difusion = False
        obj.Tipo_difusion = ' '
        obj.Resultados_periodos.delete()
        obj.Descripcion_entrega = ' '
        obj.Hay_criterios = False
        obj.Criterios_principales = ' '
        obj.Hay_programa_estimulos = False
        obj.DescripcionDifusion = ' '
        obj.save()

        return render(request, self.template_name, {'obj': obj})
