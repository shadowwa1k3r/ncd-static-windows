from django.urls import path, include

urlpatterns = [
    path('about/', include('api.about.urls')),
]
