# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from characters.mage.models import Mage
from characters.serializers import MageSerializer, UserSerializer
from characters.permissions import IsOwnerOrReadOnly


class MageList(generics.ListCreateAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)


class MageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
