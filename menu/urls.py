from django.urls import path
from menu import views

urlpatterns = [
    path('list/', views.MenuListView.as_view(), name='menu-list'),
    path('create/', views.MenuCreateView.as_view(), name='menu-create'),
    path('update/', views.MenuUpdateView.as_view(), name='menu-update'),
]