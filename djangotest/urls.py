from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^blog/', include('core.urls', namespace='core')),
    url(r'^alunos/', include('alunos.urls', namespace='alunos')),
    url(r'^turmas/', include('turmas.urls', namespace='turmas')),
    url(r'^', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
