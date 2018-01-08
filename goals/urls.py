from django.conf.urls import url

from . import views

app_name = 'goals'
urlpatterns = [
    url(r'^(?P<year>[0-9]+)/$', views.goal_list, name='goal_list'),
    url(r'^create$', views.create, name='create'),
    url(r'^detail/(?P<goals_id>[0-9]+)/$', views.detail, name='detail'),
]
