from .serializer import SuperSerializer
from .models import Super

from rest_framework import status
# from django.shortcuts import get_object_or_404
# from supers import serializer
from django.http import Http404
from rest_framework.views import APIView

from rest_framework.response import Response

class SuperList(APIView):
    def get(self, request, format=None):
        super = Super.objects.all()
        serializer = SuperSerializer(super, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class SuperDetail(APIView):
    def get_object(self, pk):
        try:
            return Super.objects.get(pk=pk)
        except Super.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        super = self.get_object(pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        super = self.get_object(pk)
        serializer = SuperSerializer(super)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        super = self.get_object(pk)
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
