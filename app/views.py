from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Informations
from .serializers import InformationsSerializer

class InformationList(APIView):
    def get(self,request):
        informations = Informations.objects.all()
        serializer = InformationsSerializer(informations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InformationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformationDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Informations, pk=pk)

    def get(self, request, pk):
        information = self.get_object(pk)
        serializer = InformationsSerializer(information)
        return Response(serializer.data)

    def put(self, request, pk):
        information = self.get_object(pk)
        serializer = InformationsSerializer(information, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        information = self.get_object(pk)
        serializer = InformationsSerializer(information, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




