from rest_framework import serializers
from .models import Informations

class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informations
        fields = '__all__'