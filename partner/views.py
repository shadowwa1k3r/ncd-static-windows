from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Partner


class PartnerListView(ListView):
    template_name = 'partner/list.html'
    model = Partner
    context_object_name = 'partners'


class PartnerCreateView(TemplateView):
    template_name = 'partner/create.html'


class PartnerUpdateView(DetailView):
    template_name = 'partner/update.html'
    model = Partner
    context_object_name = 'partner'
