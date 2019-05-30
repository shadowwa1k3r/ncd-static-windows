from django.shortcuts import render
from django.views.generic import TemplateView


class MenuListView(TemplateView):
    template_name = 'menu/list.html'


class MenuCreateView(TemplateView):
    template_name = 'menu/create.html'


class MenuUpdateView(TemplateView):
    template_name = 'menu/update.html'
