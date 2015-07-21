from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from news import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.HomeView.as_view()), name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
)
