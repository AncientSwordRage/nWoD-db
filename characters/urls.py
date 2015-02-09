from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from characters import views

urlpatterns = [
    url(r'^mages/$', views.MageList.as_view()),
    url(r'^mages/(?P<pk>[0-9]+)/$',
        views.MageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
