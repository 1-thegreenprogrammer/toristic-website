
import imp
from django.shortcuts import render
from .models import Hotel,HotelView,Resto,Agenda
def index(request):
    a="hello everyone here "
    return render(request,'pages/index.html',{'name':a})
def about(request):
    return render(request,'pages/about.html') 
def agenda(request):
    return render(request,'pages/agenda.html',{'a':Agenda.objects.all()}) 
def hotel(request):
    x={'hot':Hotel.objects.all()}
    return render(request,'pages/hotel.html',x)
def hotelView(request,pk):
    x=Hotel.objects.get(id=pk)
    
    return render(request,'pages/hotelView.html',{"s":x,"a":HotelView.objects.all()})
def resuturnat(request):
    x={'a':Resto.objects.all()}
    return render(request,"pages/resturnat.html",x)
def palces(request):
    return render(request,'pages/best.html') 
    