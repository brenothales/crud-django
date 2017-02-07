from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('turmas.views',
    # url(r'^', 'lista', name='lista'),
    url(r'^lista', 'lista', name='lista'),
    url(r'^create/$', 'create', name='create'),
    url(r'^delete/(?P<codigoTurma>\d+)$', 'delete', name='delete'),
    url(r'^update/(?P<codigoTurma>\d+)$', 'update', name='update'),
)

