from django.shortcuts import render

# Create your views here.
from .serializers import EventSerializer
from .models import Event
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def event_list(request):
    query = Event.objects.all()
    serializer = EventSerializer(query, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def event_post(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
def event_update(request, pk):
    query = Event.objects.get(id=pk)
    serializer = EventSerializer(query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def event_delete(request, pk):
    query = Event.objects.get(id=pk)
    query.delete()
    return Response("Event has been completed or deleted successfully!!")


    
    
    
