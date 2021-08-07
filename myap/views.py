from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import Mydb


def age(request):
    listage= Mydb.objects.filter(age__lt =20)
    return render(request, 'index.html', {'listage':listage})