from rest_framework import generics
from main.permissions import IsOwnerOrReadOnly
from .models import PartnerProfile
from .serializers import PartnerProfileSerializer


class PartnerProfileList(generics.ListAPIView):
    """
    - List out all the partner profiles
    """
    serializer_class = PartnerProfileSerializer
    queryset = PartnerProfile.objects.all().order_by('-created_at')
    

class PartnerProfileDetail(generics.RetrieveUpdateAPIView):
    """
    - Detail the specificly requested partner profile
    - Uses same Partner Profile serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update partner profile info
    """
    serializer_class = PartnerProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PartnerProfile.objects.all().order_by('-created_at')
