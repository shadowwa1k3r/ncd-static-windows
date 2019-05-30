from rest_framework.generics import CreateAPIView

from about.models import About
from .serializers import AboutSerializer


class AboutCreate(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
