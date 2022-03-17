from .serializer import SuperSerializer
from .models import Super
from rest_framework import generics


class SuperList(generics.ListCreateAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer


class SuperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer
