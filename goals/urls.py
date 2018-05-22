from django.conf.urls import url
from . import views

app_name = 'goals'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/', views.create, name='create'),
    url(r'^goal/(?P<pk>\d+)/$', views.goal_detail, name='goal_detail'),
    url(r'^goal/(?P<pk>\d+)/edit/$', views.goal_edit, name='goal_edit'),
    url(r'^(?P<pk>[0-9]+)/increment_goal', views.increment_goal, name='increment_goal'),
    url(r'^(?P<pk>[0-9]+)/reset_goal', views.reset_goal, name='reset_goal'),
    url(r'^(?P<pk>[0-9]+)/delete_goal', views.delete_goal, name='delete_goal'),
]
