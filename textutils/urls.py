from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('about/' , views.about, name='about'),
    path('analyze/', views.analyze, name='analyze'),
    path('Contact Us/', views.contactus, name="contactus"),
]
