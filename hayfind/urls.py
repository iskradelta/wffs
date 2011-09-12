from django.conf.urls.defaults import *

urlpatterns = patterns('hayfind.views',
    url(r'^$', 'default', name='default'),
    url(r'^settings$', 'settings',name='settings'),
    #url(r'^/search/(?P<term>\w+)$', 'find', name='hay-find'),
    #url(r'^list$', 'list', name='project-list'),
    #url(r'^(?P<project_id>\d+)/completed$', 'completed', name='project-completed'),
)
