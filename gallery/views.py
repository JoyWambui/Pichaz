from django.shortcuts import render
from . models import Image


def index(request):
    '''View function that displays uploaded photos'''
    return render(request, 'index.html')
    
