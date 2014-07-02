# -*- coding:utf-8 -*-
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import scraping

@login_required(login_url='/')
@csrf_exempt
def get_categories(request):
    if request.user.is_authenticated():
    	urls="https://owl.english.purdue.edu/owl/"
    	soup=scraping.get_soup(urls)
    	content=scraping.get_details(soup)
    	category=scraping.get_li(soup)
    	categories=scraping.get_categories_names(category)
        return render_to_response('index.html',{'categories':categories,'content':content},context_instance=RequestContext(request))

@login_required(login_url='/')
@csrf_exempt
def get_detail_categories(request,idcategory):
    if request.user.is_authenticated():
    	urls="https://owl.english.purdue.edu/owl/section/"+idcategory+'/'
    	soup=scraping.get_soup(urls)
    	content=scraping.get_details(soup)
    	category=scraping.get_li(soup)
    	categories=scraping.get_categories_names(category)
        return render_to_response('details.html',{'categories':categories,'content':content},context_instance=RequestContext(request))