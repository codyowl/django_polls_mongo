from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_polls_mongo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'polls.views.index', name='index'),
    url(r'^polls/(?P<poll_id>[\w-]+)/$', 'polls.views.detail', name='detail'),
    # url(r'^(?P<poll_id>)/results/$', views.results, name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

    url(r'^admin/', include(admin.site.urls)),
)
