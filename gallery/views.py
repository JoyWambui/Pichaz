from django.shortcuts import render
from . models import Image


def index(request):
    '''View function that displays uploaded photos'''
    images = Image.get_images()
    return render(request, 'index.html',{'images':images})
    
