from rest_framework import serializers
from .models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['VALEUR_TEMP','Timestamp']
        #fields = ['Timestamp']
   