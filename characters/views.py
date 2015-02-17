# Create your views here.
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from characters.mage.models import Mage
from characters.serializers import MageSerializer, UserSerializer
from nwod_characters.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class MageViewSet(viewsets.ModelViewSet):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'mages': reverse('mage-list', request=request, format=format)
    })
