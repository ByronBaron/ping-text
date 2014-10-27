from django.conf.urls import patterns, url
from siteapp import views
urlpatterns = patterns('', 

    url(r'^$', 'siteapp.views.home_page'),
    url(r'^text', views.TextView.as_view()),
    url(r'^ping_page/$', 'siteapp.views.ping'),
    (r'^ping_page/ping_input/$', 'siteapp.views.ping_index'),
)
