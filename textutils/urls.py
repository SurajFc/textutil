from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('about/' , views.about, name='about'),
    path('analyze/', views.analyze, name='analyze'),
    path('contact/', include('contact.urls')),
]
