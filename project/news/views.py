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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

RESULTS_PER_PAGE=20

class HomeView(View):

    def get_items(self):
        return DashboardItem.objects.select_related('item').filter(
                profile__user=self.request.user).order_by(
                    '-item__posted_on')

    def paginate_items(self, items):
        p = Paginator(items, RESULTS_PER_PAGE)
        return p

    def handle_pages(self, paginator):
        page = self.request.GET.get('page')
        try:
            return paginator.page(page)
        except PageNotAnInteger:
            return paginator.page(1)
        except EmptyPage:
            return paginator.page(paginator.num_pages)
 

    def get(self, request):
        paginator = self.paginate_items(self.get_items())
        return render(request,
            'news/home.html', {'items' : self.handle_pages(paginator)}) 

    def delete(self):
        DashboardItem.objects.filter(
                ext_id__in = self.request.POST.getlist('item_id')
            ).delete()

    def mark_as_read(self):
        items = DashboardItem.objects.filter(ext_id__in = self.request.POST.getlist('item_id'))
        for item in items:
            item.is_read = True
            item.save()

    def post(self, request):
        page = request.GET.get('page')
        paginator = self.paginate_items(self.get_items())
        if not request.POST.get('item_id'):
            return render(request, 'news/home.html', {
                'error' : 'Need to select items to perform mark read / delete!', 
                'items' : self.handle_pages(paginator) 
            })

        if 'delete' in request.POST:
            self.delete()
        else:
            self.mark_as_read()
        return HttpResponseRedirect('/news/')
        


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = UserProfile.objects.create(user = user)
            registered = True
            for item in Item.objects.all():
                DashboardItem.objects.create(item = item, profile = profile)
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

