from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
