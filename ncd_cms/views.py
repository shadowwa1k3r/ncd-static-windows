from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

