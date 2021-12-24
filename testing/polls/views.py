from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def test(request):
    return HttpResponse("<h1>Hello, world. You're at the polls test.</h1>") #looks like can take in html tags
