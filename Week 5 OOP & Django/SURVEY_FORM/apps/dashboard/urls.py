from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process/$', views.process, name='process'),
    url(r'^success/$', views.success, name='success'),
    url(r'^colors/(?P<color>\w+)$', views.colors, name='colors'),
    url(r'^user_ids/(?P<u_id>\d+)$', views.user_ids, name='user_ids')
]