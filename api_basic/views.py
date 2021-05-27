from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Temperature
from .serializers import TemperatureSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#import sqlite3

# Create your views here.

#connection = sqlite3.connect('ambiance.db')

#cursor = connection.cursor()

@api_view(['GET','POST'])

def liste_temperature(request): 

    if request.method == 'GET': 
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures,many=True) #serialier un qeury set
        return Response(serializer.data)#on retourne la reponse en format json


    elif request.method == 'POST': 
        serializer = TemperatureSerializer(data=request.data) #on passe les données4
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET','PUT','DELETE'])
    def details_temp(request, pk):
        try:
            temperature = Temperature.objects.get(pk=pk)

        except Temperature.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
        
        if request.method == 'GET':
            serializer = TemperatureSerializer(temperature)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TemperatureSerializer(temperature,data=request.data) #on passe les données4
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method =='DELETE':
            temperature.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        

