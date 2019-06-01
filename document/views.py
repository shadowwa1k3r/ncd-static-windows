from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Document


class DocumentListView(ListView):
    template_name = 'document/list.html'
    model = Document
    context_object_name = 'documents'


class DocumentCreateView(TemplateView):
    template_name = 'document/create.html'


class DocumentUpdateView(DetailView):
    template_name = 'document/update.html'
    model = Document
    context_object_name = 'document'
