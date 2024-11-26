from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> king koli is the team capatain for rcb</h1>')

def vicecaptain(request):
    return HttpResponse('<h1> Dhawan is the vicecaptain </h1> ')
