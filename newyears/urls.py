from django.conf.urls import url

from . import views

app_name = 'newyears'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<newyear_id>[0-9]+)/$', views.newyear_detail, name='newyear_detail'),
    url(r'^(?P<newyear_id>[0-9]+)/newlist$', views.list_create, name='list_create'),
    url(r'^(?P<newyear_id>[0-9]+)/list/(?P<list_id>[0-9]+)$', views.list_detail, name='list_detail'),
]

