from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Details

# Create your views here.

def hello(request):
    #return HttpResponse("Hello world")
    data=Details.objects.all()
    return render(request,'hello.html',{"data":data})


