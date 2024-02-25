from rest_framework import serializers
from .models import Passion

class PassionListSerializer(serializers.ModelSerializer):

    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Passion
        fields = ['owner', 'id', 'partner_profile',
                  'passion_text', 'is_owner',]
        

class PassionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    partner_profile = serializers.ReadOnlyField(source='partner_profile.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Passion
        fields = ['owner', 'id', 'partner_profile',
                  'passion_text', 'is_owner',]