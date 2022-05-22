from django import http
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html', {'password':'Prathmesh@20'})

def password(request):
    charectors = list('abcdefghijklmnopqrstuvwxyz')

    if(request.GET.get('uppercase')):
        charectors.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if(request.GET.get('special')):
        charectors.extend(list('!@#$%&*'))

    if(request.GET.get('numbers')):
        charectors.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(charectors)
    
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
