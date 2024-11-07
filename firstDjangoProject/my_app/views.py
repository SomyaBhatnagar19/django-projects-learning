from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# creating an online newspaper thing

def sports_view(request):
    return HttpResponse("Sports Page")

def finance_view(request):
    return HttpResponse("Finance Page")