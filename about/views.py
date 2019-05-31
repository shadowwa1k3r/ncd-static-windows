from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View
from .models import About


class AboutListView(ListView):
    template_name = 'about/list.html'
    model = About
    context_object_name = 'abouts'


class AboutCreateView(TemplateView):
    template_name = 'about/create.html'


class AboutUpdateView(TemplateView):
    template_name = 'about/update.html'


class AboutDeleteView(View):
    def post(self, request):
        id = self.request.POST.get('about_id')
        about = About.objects.get(id=id)
        about.delete()
        return HttpResponseRedirect(reverse('about-list'))
