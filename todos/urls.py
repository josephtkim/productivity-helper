from django.conf.urls import url
from . import views

app_name = 'todos'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/', views.create, name='create'),
    url(r'^clear_completed/', views.clear_completed, name='clear_completed'),
    url(r'^(?P<pk>[0-9]+)/mark_complete', views.mark_complete, name='mark_complete'),
    url(r'^(?P<pk>[0-9]+)/unmark_complete', views.unmark_complete, name='unmark_complete'),
    url(r'^(?P<pk>[0-9]+)/delete_todo', views.delete_todo, name='delete_todo'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
]
