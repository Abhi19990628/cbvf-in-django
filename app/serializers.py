from rest_framework import serializers
from .models import Informations,Student,Collages,Teacher


class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informations
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class CollagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collages
        fields = '__all__'
        
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields ='__all__'