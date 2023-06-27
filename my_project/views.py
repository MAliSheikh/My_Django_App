from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(reuqest):
    return render(reuqest,'home.html')

