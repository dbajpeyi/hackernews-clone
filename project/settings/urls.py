from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^openid/(.*)', SessionConsumer()),
)
