from rest_framework import serializers
from .models import UserProfile



class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model
    Owner shows object owner's username in readonly format
    Get function to set is_owner to true/false
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    bio = serializers.ReadOnlyField()

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = UserProfile
        fields = [
            'is_owner', 'id', 'owner',
            'created_at', 'bio', 'image',
            'created_at',
        ]
