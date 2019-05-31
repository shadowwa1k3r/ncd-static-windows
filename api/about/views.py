from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from about.models import About
from .serializers import AboutSerializer


class AboutCreate(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutUpdate(UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    lookup_url_kwarg = 'id'


class AboutDelete(APIView):
    def post(self, request):
        about_id = request.data.get('about_id')
        about = About.objects.get(id=about_id)
        about.delete()
        return Response(status=200)
