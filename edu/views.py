from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Edu


class EduListView(ListView):
    template_name = 'edu/list.html'
    model = Edu
    context_object_name = 'edus'


class EduCreateView(TemplateView):
    template_name = 'edu/create.html'


class EduUpdateView(DetailView):
    template_name = 'edu/update.html'
    model = Edu
    context_object_name = 'edu'
