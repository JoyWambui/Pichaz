from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('search/', views.search_categories, name='search_categories'),
    path('locations/', views.locations, name='locations'),
    path('locations/<int:id>', views.location_images, name='location_images')
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)