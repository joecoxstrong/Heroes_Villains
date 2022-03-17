
from .serializers import SuperTypesSerializer
from .models import SuperTypes
from rest_framework import generics


class SuperTypesList(generics.ListCreateAPIView):
    queryset = SuperTypes.objects.all()
    serializer_class = SuperTypesSerializer


class SuperTypesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperTypes.objects.all()
    serializer_class = SuperTypesSerializer