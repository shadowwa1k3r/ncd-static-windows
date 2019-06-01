from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from edu.models import Edu
from .serializers import EduSerializer


class EduCreate(CreateAPIView):
    queryset = Edu.objects.all()
    serializer_class = EduSerializer


class EduUpdate(UpdateAPIView):
    queryset = Edu.objects.all()
    serializer_class = EduSerializer
    lookup_url_kwarg = 'id'


class EduDelete(DestroyAPIView):
    queryset = Edu.objects.all()
    lookup_url_kwarg = 'id'
