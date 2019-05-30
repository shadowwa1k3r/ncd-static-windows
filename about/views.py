from django.shortcuts import render
from django.views.generic import TemplateView


class AboutListView(TemplateView):
    template_name = 'about/list.html'


class AboutCreateView(TemplateView):
    template_name = 'about/create.html'


class AboutUpdateView(TemplateView):
    template_name = 'about/update.html'
