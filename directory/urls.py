from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^album/(?P<pk>[1-9])+/$', views.AlbumView.as_view(), name="album"),
]
