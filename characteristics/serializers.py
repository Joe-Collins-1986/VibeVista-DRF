from rest_framework import serializers
from .models import Characteristic



class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['id', 'description']