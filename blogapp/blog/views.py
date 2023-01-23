from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Home Page") # ana sayfa yazısı çıksın istiyorum 

def blogs(request):    
    return HttpResponse("Blogs") # 

def blogdetails(request,id):
     return HttpResponse("Blog Details"+str(id))
