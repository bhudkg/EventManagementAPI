from django.shortcuts import render

# Create your views here.
from .serializers import EventSerializer
from .models import Event
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status


# @api_view(['GET'])
# def event_list(request):
#     query = Event.objects.all()
#     serializer = EventSerializer(query, many=True)
#     return Response(serializer.data)

class EventView(APIView):
    
    def get(self, request):
        query = Event.objects.all()
        serializer = EventSerializer(query, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        query = Event.objects.get(id=pk)
        serializer = EventSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        query = Event.objects.get(id=pk)
        query.delete()
        return Response("Event has been completed or deleted successfully!!")


# @api_view(['POST'])
# def event_post(request):
#     serializer = EventSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(['PATCH'])
# def event_update(request, pk):
#     query = Event.objects.get(id=pk)
#     serializer = EventSerializer(query, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(['DELETE'])
# def event_delete(request, pk):
#     query = Event.objects.get(id=pk)
#     query.delete()
#     return Response("Event has been completed or deleted successfully!!")


    
    
    
