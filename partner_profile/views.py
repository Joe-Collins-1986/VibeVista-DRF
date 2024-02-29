from django.shortcuts import get_object_or_404
from rest_framework import generics
from main.permissions import IsPrimaryProfileOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import PartnerProfile
from user_profile.models import UserProfile
from .serializers import PartnerProfileListSerializer, PartnerProfileDetailSerializer



class PartnerProfileList(generics.ListCreateAPIView):
    """
    - List out all the partner profiles
    """
    serializer_class = PartnerProfileListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PartnerProfile.objects.filter(primary_profile=user).order_by('-created_at')
    
    def perform_create(self, serializer):
        # Save the PartnerProfile with the current user set as the primary_profile
        serializer.save(primary_profile=self.request.user)

        # Check if this is the user's first partner profile
        user_profile, created = UserProfile.objects.get_or_create(owner=self.request.user)
        if user_profile.active_partner_profile_id is None:
            # Set the active_partner_profile_id to the id of the newly created PartnerProfile
            user_profile.active_partner_profile_id = serializer.instance.id
            user_profile.save()
    

class PartnerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested partner profile
    - Uses same Partner Profile serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update partner profile info
    """
    serializer_class = PartnerProfileDetailSerializer
    permission_classes = [IsAuthenticated, IsPrimaryProfileOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return PartnerProfile.objects.filter(primary_profile=user).order_by('-created_at')
    
    def destroy(self, request, *args, **kwargs):
        partner_profile = self.get_object()
        user_profile = get_object_or_404(UserProfile, owner=partner_profile.primary_profile)

        # Check if the deleted PartnerProfile is the active one before performing the delete operation
        is_active_profile = (user_profile.active_partner_profile_id == partner_profile.id)
        
        # Perform the deletion using the superclass's destroy method
        response = super().destroy(request, *args, **kwargs)

        # If the deleted PartnerProfile was the active one, update the UserProfile
        if is_active_profile:
            user_profile.active_partner_profile_id = None
            user_profile.save()

        return response
