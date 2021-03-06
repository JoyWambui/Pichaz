from django.http import Http404
from django.shortcuts import render
from . models import Image,Category,Location
from django.contrib import messages


def index(request):
    '''View function that displays uploaded photos'''
    images = Image.get_images()
    return render(request, 'index.html',{'images':images})

def search_categories(request):
    '''View function that displays searched photos by category'''
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        messages.add_message(request, messages.ERROR, "You haven't searched for any term.")
        return render(request, 'search.html')
    
def locations(request):
    '''View function that displays all locations'''
    locations= Location.get_locations()
    return render(request,'locations.html',{'locations':locations})

def location_images(request,id):
    '''View function that displays all images based on a location'''
    try:
        location = Location.objects.get(id = id)
    except Location.DoesNotExist:
        raise Http404("Location does not exist")
    images = Image.view_by_location(location.location_name)
    return render(request,"location.html", {"images":images, 'location':location})