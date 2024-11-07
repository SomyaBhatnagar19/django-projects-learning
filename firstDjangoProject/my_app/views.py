from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# creating an online newspaper thing

#using a dictionary python object

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

def sports_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse(articles['finance'])

def politics_view(request):
    return HttpResponse(articles['politics'])