from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def blogs(request):
    template = loader.get_template('blogs.html')
    return HttpResponse(template.render())