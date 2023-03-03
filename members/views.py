from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context ={
        'mymembers' : mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('detail.html')
    context ={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def testing(request):
    mydata=Member.objects.all().filter(fname__startswith='D').values()
    template = loader.get_template('test.html')
    context ={
        'code':mydata,
    }
    return HttpResponse(template.render(context,request))
