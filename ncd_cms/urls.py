from django.urls import path
from ncd_cms import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]