from rest_framework import serializers
from .models import PartnerProfile
from characteristics.models import Characteristic
from characteristics.serializers import CharacteristicSerializer

class PartnerProfileListSerializer(serializers.ModelSerializer):
    characteristics = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Characteristic.objects.all(), required=False)
    characteristics_display = CharacteristicSerializer(many=True, read_only=True, source='characteristics')

    class Meta:
        model = PartnerProfile
        fields = ['id', 'primary_profile', 'name', 'about', 'image', 'created_at', 'characteristics', 'characteristics_display']
        

class PartnerProfileDetailSerializer(serializers.ModelSerializer):
    primary_profile = serializers.ReadOnlyField(source='primary_profile.username')
    is_owner = serializers.SerializerMethodField()
    characteristics = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Characteristic.objects.all(), write_only=True, required=False)
    characteristics_display = CharacteristicSerializer(many=True, read_only=True, source='characteristics')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.primary_profile
    
    def update(self, instance, validated_data):
        characteristics = validated_data.pop('characteristics', None)
        if characteristics is not None:
            instance.characteristics.set(characteristics)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = PartnerProfile
        fields = [
            'is_owner', 'id', 'primary_profile',
            'name', 'about', 'image',
            'created_at', 'characteristics', 'characteristics_display', 
            ]