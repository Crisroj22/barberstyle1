from django.shortcuts import render
from django import forms


def indice(request):
    return render(request, '../templates/extranet/index.html')

# Create your views here.
