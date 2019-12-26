from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import variable
from .serializers import ValueSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(["GET", "POST"])
def showList(request):
    if(request.method == "GET"):
        data = variable.objects.all()
        serializers = ValueSerializer(data, many=True)
        return Response(serializers.data)
    elif(request.method == "POST"):
        serializer = ValueSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
