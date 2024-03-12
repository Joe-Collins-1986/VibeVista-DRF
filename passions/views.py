from rest_framework import generics
from main.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Passion
from .serializers import PassionListSerializer, PassionSerializer



class PassionList(generics.ListCreateAPIView):
    """
    - List out all the partner profiles
    """
    serializer_class = PassionListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Passion.objects.filter(owner=user)
    

class PassionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested partner profile
    - Uses same Partner Profile serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update partner profile info
    """
    serializer_class = PassionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Passion.objects.all()
