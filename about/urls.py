from django.urls import path
from about import views

urlpatterns = [
    path('list/', views.AboutListView.as_view(), name='about-list'),
    path('create/', views.AboutCreateView.as_view(), name='about-create'),
    path('update/', views.AboutUpdateView.as_view(), name='about-update'),
]