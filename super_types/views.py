from rest_framework.decorators import api_view
from rest_framework.response import Response
from supers.models import Super

# import super_types
# from supers.models import Super
from supers.serializer import SuperSerializer
from .serializers import SuperTypesSerializer
from .models import SuperTypes
from rest_framework import status
from django.shortcuts import get_object_or_404
# from super_types import serializers
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework import generics




@api_view(['GET','POST'])
def SuperTypesList(request):  

    if request.method == 'GET':
        super_type = SuperTypes.objects.all()
        serializer = SuperTypesSerializer(super_type, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperTypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])       
def SuperTypeDetail(request,pk):
    super_type = get_object_or_404(SuperTypes, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypesSerializer(super_type);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypesSerializer(super_type, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    


# from .serializers import SuperTypesSerializer
# from .models import SuperTypes
# from rest_framework import generics



# class SuperTypesList(generics.ListCreateAPIView):
#     queryset = SuperTypes.objects.all()
#     serializer_class = SuperTypesSerializer


# class SuperTypesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SuperTypes.objects.all()
#     serializer_class = SuperTypesSerializer