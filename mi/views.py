from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1> virat is the team capatain for rcb</h1>')

def vicecaptain(request):
    return HttpResponse('<h1> hardik pandya is the vicecaptain </h1> ')
