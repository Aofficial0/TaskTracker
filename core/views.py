from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def taskTrack(request):
    return HttpResponse("Hello, Core!")