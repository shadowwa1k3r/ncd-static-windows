from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('about/', include('api.about.urls')),
]
