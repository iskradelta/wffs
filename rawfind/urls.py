from django.conf.urls.defaults import *

urlpatterns = patterns('wffs.rawfind.views',
    #url(r'^$', 'default', name='default'),
    #url(r'^(?P<project_id>\d+)/$', 'detail',name='project-detail'),
    url(r'^/search/(?P<term>\w+)$', 'find',name='raw-find'),
    #url(r'^list$', 'list', name='project-list'),
    #url(r'^(?P<project_id>\d+)/completed$', 'completed', name='project-completed'),
)
