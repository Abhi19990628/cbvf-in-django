from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Informations,Student,Collages
from .serializers import InformationsSerializer,StudentSerializer,CollagesSerializer

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


   def delete(self, request, pk):
        information = self.get_object(pk)
        information.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    

#########________________Student apis__________________#############
   #____________________________________________________________#

<<<<<<< HEAD


class Studentinformation(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)
    
    def get(self, request, pk):
        student  = self.get_object(pk)
        serializer = InformationsSerializer(student)
        return Response(serializer.data)
    
#########_______________________collages________________________#############
#___________________________________________________________________________#


class collagesinformations(APIView):
    def get(self, request):
        collages=Collages.objects.all()
        serializer=CollagesSerializer(collages , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CollagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
=======
>>>>>>> c35c5e9711ed068ff39ac206051d6f183edd439a
