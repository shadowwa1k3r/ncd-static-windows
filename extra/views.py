from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Extra


class ExtraListView(ListView):
    template_name = 'extra/list.html'
    model = Extra
    context_object_name = 'extras'


class ExtraCreateView(TemplateView):
    template_name = 'extra/create.html'


class ExtraUpdateView(DetailView):
    template_name = 'extra/update.html'
    model = Extra
    context_object_name = 'extra'
