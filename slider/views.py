from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Slider


class ServiceListView(ListView):
    template_name = 'slider/list.html'
    model = Slider
    context_object_name = 'sliders'


class ServiceCreateView(TemplateView):
    template_name = 'slider/create.html'


class ServiceUpdateView(DetailView):
    template_name = 'slider/update.html'
    model = Slider
    context_object_name = 'slider'
