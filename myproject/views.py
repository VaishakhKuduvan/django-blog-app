#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("Hello world im home baby")
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("My about page")
    return render(request, 'about.html')
