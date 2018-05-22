from django.conf.urls import url
from . import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^create/', views.create, name='create'),
    url(r'^entry/(?P<pk>\d+)/$', views.entry_detail, name="entry_detail"),
    url(r'^entry/(?P<pk>\d+)/edit/$', views.entry_edit, name="entry_edit"),
    url(r'^entry/new/$', views.entry_new, name="entry_new"),
    url(r'^(?P<pk>\d+)/entry_delete/$', views.entry_delete, name="entry_delete"),
]
