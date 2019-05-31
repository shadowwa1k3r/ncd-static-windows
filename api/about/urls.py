from django.urls import path

from api.about.views import AboutCreate

urlpatterns = [
    path('create/', AboutCreate.as_view(), name='about-create-api'),
]
