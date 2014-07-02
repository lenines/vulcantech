# -*- coding:utf-8 -*-
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from forms import LoginForm

def signin(request):    
    message = ''
    if request.method == 'POST': 
        form = LoginForm(request.POST) 
        if form.is_valid():
            login_username = form.cleaned_data['login_username']
            login_password = form.cleaned_data['login_password']
            user = authenticate(username=login_username, password=login_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        return HttpResponseRedirect('/server1/')
                    else:
                        return HttpResponseRedirect('/server2/')
                else:
                    message='User is disabled'
            else:
                message="Invalid User"
        else:
            message = 'Please enter your username and password.'
    else:
        form = LoginForm()

    return render(request, 'signin.html', {
        'message': message,
        'login_username': '',
        'form': form,
    })

@login_required(login_url='/')
@csrf_exempt
def home(request):
    if request.user.is_authenticated():
        return render_to_response('master.html', context_instance=RequestContext(request))

@login_required(login_url='/')
@csrf_exempt
def server1(request):
    if request.user.is_authenticated():
        return render_to_response('server1.html', context_instance=RequestContext(request))

@login_required(login_url='/')
@csrf_exempt
def server2(request):
    if request.user.is_authenticated():
        return render_to_response('server2.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def close_session(request):
    logout(request)
    return HttpResponseRedirect('/')
            