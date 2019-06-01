from django.urls import path
from slider import views

urlpatterns = [
    path('list/', views.ServiceListView.as_view(), name='slider-list'),
    path('create/', views.ServiceCreateView.as_view(), name='slider-create'),
    path('update/<int:pk>', views.ServiceUpdateView.as_view(), name='slider-update'),
]
