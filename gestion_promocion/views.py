from django.shortcuts import render

# Create your views here.

def promocion(request):
    return render(request, 'promocion/promocion.html')

