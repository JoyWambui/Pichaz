from django.shortcuts import render

def index(request):
    '''View function that displays uploaded photos'''
    return render(request, 'index.html')
    
