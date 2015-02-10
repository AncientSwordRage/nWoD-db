# Create your views here.
from characters.mage.models import Mage
from characters.serializers import MageSerializer
from rest_framework import generics


class MageList(generics.ListCreateAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer


class MageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer
