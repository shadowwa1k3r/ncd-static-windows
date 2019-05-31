from django.urls import path, include

urlpatterns = [
    path('about/', include('api.about.urls')),
    path('service/', include('api.service.urls')),
    path('partner/', include('api.partner.urls')),
    path('feedback/', include('api.feedback.urls')),
    path('employee/', include('api.employee.urls')),
]
