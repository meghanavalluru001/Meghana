from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hash(request):
    return HttpResponse('Hello Mr.Hash')