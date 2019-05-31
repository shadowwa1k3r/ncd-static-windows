from django.urls import reverse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Feedback


class FeedbackListView(ListView):
    template_name = 'feedback/list.html'
    model = Feedback
    context_object_name = 'feedbacks'


class FeedbackCreateView(TemplateView):
    template_name = 'feedback/create.html'


class FeedbackUpdateView(DetailView):
    template_name = 'feedback/update.html'
    model = Feedback
    context_object_name = 'feedback'
