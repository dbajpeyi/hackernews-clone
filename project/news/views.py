from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import View
import requests
from news.models import *
from news.forms import UserForm

class HomeView(View):

    def get(self, request):
        return render(request,
            'news/home.html', {}) 
        


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            UserProfile.objects.create(user = user)
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()


    return render(request,
            'news/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/news/')
            else:
                return HttpResponse("Your user account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, "news/login.html", {"error" : "Invalid login details"})

    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/news') 
        return render(request, 'news/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/news/')

