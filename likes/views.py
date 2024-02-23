from rest_framework import generics
from .models import Like
from .serializers import LikeSerializer

class LikesList(generics.ListAPIView):
    """
    - List out all the likes
    """
    serializer_class = LikeSerializer
    queryset = Like.objects.all()