from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cool.views.home', name='home'),
    # url(r'^cool/', include('cool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'private_courses/', include('private_course.urls'))
)

# if settings.DEBUG:
#   urlpatterns += patterns('',
#                          (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
#                           'django.views.static.serve',
#                           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#   ) 
