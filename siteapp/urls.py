from django.conf.urls import patterns, url
urlpatterns = patterns('', 

    url(r'^$', 'siteapp.views.home_page'),
    url(r'^text', 'siteapp.views.text'),
    url(r'^ping_page/$', 'siteapp.views.ping'),
    (r'^ping_page/ping_input/$', 'siteapp.views.ping_index'),
)
