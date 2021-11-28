from django.shortcuts import render

def home(request):
    '''View function that displays uploaded photos'''
    return render(request, 'home.html')
    
