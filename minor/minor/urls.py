from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from . import views

# use paranthesis to capture arguments from the url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view(), name='HomePage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # url(r'^hello/$', hello),
)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
))
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)