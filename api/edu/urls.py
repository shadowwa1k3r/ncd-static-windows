from django.urls import path

from api.edu.views import EduCreate, EduUpdate, EduDelete

urlpatterns = [
    path('create/', EduCreate.as_view(), name='edu-create-api'),
    path('delete/<int:id>', EduDelete.as_view(), name='edu-delete-api'),
    path('update/<int:id>', EduUpdate.as_view(), name='edu-update-api'),
]
