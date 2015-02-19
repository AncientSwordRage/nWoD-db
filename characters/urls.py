from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from characters.views import UserViewSet, MageViewSet, api_root, IndexView

mage_list = MageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
mage_detail = MageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    url(r'^api/root$', api_root),
    url(r'^api/mages$', mage_list, name='mage-list'),
    url(r'^api/mages/(?P<pk>[0-9]+)$', mage_detail, name='mage-detail'),
    url(r'^api/users$', user_list, name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)$', user_detail, name='user-detail'),
    url(r'^.*$', IndexView.as_view(), name='index'),
])
