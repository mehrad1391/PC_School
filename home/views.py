from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

class CoursesListApiView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = courseserializersapiview

class SessionsListApiView(generics.ListAPIView):
    queryset = session.objects.all()
    serializer_class = sessionsserializersapiview