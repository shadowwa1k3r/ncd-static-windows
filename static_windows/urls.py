from django.urls import path
from static_windows import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]