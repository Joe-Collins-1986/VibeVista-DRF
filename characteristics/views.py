from rest_framework import generics
from .models import Characteristic
from .serializers import CharacteristicSerializer

class CharacteristicList(generics.ListAPIView):
    """
    - List out all the characteristics
    """
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()