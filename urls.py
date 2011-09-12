from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wffs.hayfind.views.default', name='home'),
    url(r'^search', 'hayfind.views.find', name='hay-find'),
    url(r'^about', 'hayfind.views.about', name='about'),
    url(r'^contact', 'hayfind.views.contact', name='contact'),
    url(r'^adv_search', 'hayfind.views.adv_search', name='adv_search'),
    url(r'^updatedb', 'hayfind.views.updatedb', name='raw-update'),
    (r'^', include('hayfind.urls')),
    (r'^rawfind/', include('rawfind.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^wffs/admin/', include(admin.site.urls)),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #       {'document_root': '/home/anto/Development/projects/scrumSite/static'}),

)
