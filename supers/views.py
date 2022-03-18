from rest_framework.decorators import api_view
from rest_framework.response import Response

# import super_types
from super_types.serializers import SuperTypesSerializer
from supers.models import Super
from supers.serializer import SuperSerializer
# from .serializers import SuperTypesSerializer
from .models import SuperTypes
from rest_framework import status
from django.shortcuts import get_object_or_404
# from super_types import serializers
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework import generics




@api_view(['GET','POST'])
def SuperList(request):
       
    super_types_param = request.query_params.get('type')
    sort_param = request.query_params.get('sort')

    supers = Super.objects.all()
    if super_types_param:
        supers = supers.filter(super_type__type=super_types_param)
    else:
        super_types = SuperTypes.objects.all()
        custom_response_dictionary = {}

        for super_type in super_types:
            supers = Super.objects.filter(super_type__type = super_type.type)

            super_serializer = SuperSerializer(supers, many = True)

            custom_response_dictionary[super_type.type] = super_serializer.data
            # 'type': super_type.type,
            # 'supers': super_serializer.data 
        
        return Response(custom_response_dictionary) 
    if sort_param:
        supers = supers.order_by(sort_param)   
    serializer=SuperSerializer(supers,many=True)    
    return Response(serializer.data)

    if request.method == 'GET':
        super = Super.objects.all()
        serializer = SuperSerializer(super, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])       
def SuperDetail(request,pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 






# from .serializer import SuperSerializer
# from .models import Super

# from rest_framework import status
# # from django.shortcuts import get_object_or_404
# # from supers import serializer
# from django.http import Http404
# from rest_framework.views import APIView

# from rest_framework.response import Response

# class SuperList(APIView):
    
#     def get(self, request, format=None):
#         super = Super.objects.all()
#         serializer = SuperSerializer(super, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SuperSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

# class SuperDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Super.objects.get(pk=pk)
#         except Super.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         super = self.get_object(pk)
#         serializer = SuperSerializer(super)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         super = self.get_object(pk)
#         serializer = SuperSerializer(super, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         super = self.get_object(pk)
#         super.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
