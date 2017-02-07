from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('alunos.views',
    # url(r'^$', 'lista', name='lista'),
    url(r'^$', 'lista', name='lista'),
    url(r'^create/$', 'create', name='create'),
    url(r'^delete/(?P<codigoAluno>\d+)$', 'delete', name='delete'),
    url(r'^update/(?P<codigoAluno>\d+)$', 'update', name='update'),
)
