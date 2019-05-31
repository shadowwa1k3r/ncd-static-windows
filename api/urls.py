from django.urls import path, include

urlpatterns = [
    path('about/', include('api.about.urls')),
    path('service/', include('api.service.urls')),
    path('partner/', include('api.partner.urls')),
]
