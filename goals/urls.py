from django.conf.urls import url

from . import views

app_name = 'goals'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<goals_id>[0-9]+)/$', views.detail, name='detail'),
]
