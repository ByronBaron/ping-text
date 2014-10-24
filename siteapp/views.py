from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from subprocess import Popen
# Create your views here.
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

@login_required(login_url='/login/')
def ping(request):
    return render_to_response('siteapp/ping_page.html')

@login_required(login_url='/login/')
def ping_index(request):
    var = input("Enter a site: ")
    p = Popen(["ping", "-c", "7", var])
    return render_to_response('siteapp/ping_input.html', p)

#text views
@login_required(login_url='/login/')
def text(request):
    return render_to_response('siteapp/text_display.html')
