from rest_framework import serializers
from .models import PartnerProfile



class PartnerProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the PartnerProfile model
    Owner shows object owner's username in readonly format
    Get function to set is_owner to true/false
    """
    primary_profile = serializers.ReadOnlyField(source='primary_profile.username')

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.primary_profile

    class Meta:
        model = PartnerProfile
        fields = [
            'is_owner', 'id', 'primary_profile',
            'name', 'about', 'image',
            'characteristics', 'likes',
            'created_at',    ]