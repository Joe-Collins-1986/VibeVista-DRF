from rest_framework import generics
from main.permissions import IsPrimaryProfileOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import PartnerProfile
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
    

class PartnerProfileDetail(generics.RetrieveUpdateAPIView):
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
