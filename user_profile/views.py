
from rest_framework import generics
from main.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileList(generics.ListAPIView):
    """
    - List out all the profiles
    - Account created by user registration so no create
    account required
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        return UserProfile.objects.filter(owner=user).order_by('-created_at')

    

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    """
    - Detail the specificly requested profile
    - Uses same UserProfile serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update profile info
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):

        user = self.request.user
        return UserProfile.objects.filter(owner=user).order_by('-created_at')
