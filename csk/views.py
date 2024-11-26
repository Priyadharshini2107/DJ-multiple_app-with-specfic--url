from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> rujuraj is the team capatain for csk</h1>')

def Dhoni(request):
    return HttpResponse('<h1> MS.Dhoni the backbone of csk team</h1>')

