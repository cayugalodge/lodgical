from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lodgical.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name="home"),
    url(r'^about/$', 'web.views.about', name="about"),
    url(r'^alumni/$', 'web.views.alumni', name="alumni"),
    url(r'^alumni/add/$', 'web.views.add_alum', name="add_alum"),
    url(r'^mosey/$', 'web.views.mosey', name="mosey"),
    url(r'^mosey/add/$', 'web.views.add_mosey', name="mosey_add"),
    url(r'^mosey/decision/$', 'web.views.mosey_view', name="view_moseyers"),
    url(r'^mosey/thanks/$', TemplateView.as_view(template_name="mosey_thanks.html"), name="mosey_thanks"),
    url(r'^contact/$', 'web.views.contact', name="contact"),
    url(r'^lodgical/$', TemplateView.as_view(template_name="lodgical.html"), name="lodgical_home"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root', settings.STATIC_ROOT}),
)
