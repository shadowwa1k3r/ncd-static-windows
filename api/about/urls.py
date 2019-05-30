from django.urls import path

from api.about.views import AboutCreate

app_name = 'about'

urlpatterns = [
    path('create/', AboutCreate.as_view(), name='about-create-api'),
]
