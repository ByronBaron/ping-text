from django.conf.urls import patterns, include, url
from django.contrib import admin
from siteapp import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mikesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/',include('siteapp.urls')),
    url(r'^login/$', 'siteapp.views.login_user'),
)
