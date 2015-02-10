from django.conf.urls import patterns, include, url
from django.contrib import admin
from characters import views
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'nwod_characters.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('characters.urls')),
                       url(r'^users/$', views.UserList.as_view()),
                       url(r'^users/(?P<pk>[0-9]+)/$',
                           views.UserDetail.as_view()),
                       )
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
