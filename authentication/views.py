from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return HttpResponse("hello I am World")

def signup(request):
    return render("authentication/signup.html")

def signin(request):
    return render("authentication/signin.html")

def signout(request):
    pass