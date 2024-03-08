from rest_framework import serializers
from .models import PartnerProfile
from characteristics.models import Characteristic
from characteristics.serializers import CharacteristicSerializer
from likes.models import Like
from likes.serializers import LikeSerializer
from passions.serializers import PassionSerializer

class PartnerProfileListSerializer(serializers.ModelSerializer):
    characteristics = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Characteristic.objects.all(), write_only=True, required=False)
    characteristics_display = CharacteristicSerializer(many=True, read_only=True, source='characteristics')

    likes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Like.objects.all(), write_only=True, required=False)
    likes_display = LikeSerializer(many=True, read_only=True, source='likes')

    passions = PassionSerializer(many=True, read_only=True)

    is_primary_profile = serializers.SerializerMethodField()

    def get_is_primary_profile(self, obj):
        request = self.context['request']
        return request.user == obj.primary_profile

    class Meta:
        model = PartnerProfile
        fields = ['is_primary_profile', 'id', 'primary_profile',
                  'name', 'relationship', 'date_of_birth', 'gender',
                  'image', 'created_at',
                  'characteristics', 'characteristics_display',
                  'likes', 'likes_display', 'passions' ]
        

class PartnerProfileDetailSerializer(serializers.ModelSerializer):
    primary_profile = serializers.ReadOnlyField(source='primary_profile.username')
    is_primary_profile = serializers.SerializerMethodField()
    characteristics = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Characteristic.objects.all(), write_only=True, required=False)
    characteristics_display = CharacteristicSerializer(many=True, read_only=True, source='characteristics')
    likes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Like.objects.all(), write_only=True, required=False)
    likes_display = LikeSerializer(many=True, read_only=True, source='likes')
    passions = PassionSerializer(many=True, read_only=True)

    def get_is_primary_profile(self, obj):
        request = self.context['request']
        return request.user == obj.primary_profile
    
    def update(self, instance, validated_data):
        characteristics = validated_data.pop('characteristics', None)
        likes = validated_data.pop('likes', None)

        if characteristics is not None:
            instance.characteristics.set(characteristics)
        if likes is not None:
            instance.likes.set(likes)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = PartnerProfile
        fields = [
            'is_primary_profile', 'id', 'primary_profile',
            'name', 'relationship', 'date_of_birth', 'gender', 'image',
            'created_at', 'characteristics', 'characteristics_display', 
            'likes', 'likes_display', 'passions' ]