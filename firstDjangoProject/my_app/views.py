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

# dynamically updating the views

def news_view(request,topic): # topic -> dynamic variable
    return HttpResponse(articles[topic])

def add_view(request,num1,num2):
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(result)