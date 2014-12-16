from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from subprocess import Popen
from django.views import generic
from siteapp.models import Text
import json
# Create your views here.

#login view
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('siteapp/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def home_page(request):
    return render_to_response('siteapp/home.html')

#ping views

@login_required(login_url='/login/')
def ping(request):
    return render_to_response('siteapp/ping_page.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ping_index(request):
    x = [1, 2, 3, 4, 5]
    json.dumps(x)
    return render_to_response('siteapp/ping_input.html', x)

#text views

class TextView(generic.ListView): 
    model = Text
    template_name  = "siteapp/text_display.html"

