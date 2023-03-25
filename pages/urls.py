from django.urls import path
from . import views

urlpatterns=[
path('index',views.index,name='index'),
path('about',views.about,name='about'),
path('agenda',views.agenda,name='agenda'),
path('hotel',views.hotel,name='hotel'),
path('hotel/<str:pk>',views.hotelView,name='hotelname'),
path('resturnat',views.resuturnat,name='resturnat'),
path('places',views.palces,name='places'),



]