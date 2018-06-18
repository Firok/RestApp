from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^restaurants/$', views.restaurant_api),
    url(r'^address/$', views.address_api),
    url(r'^$', views.index, name='index'),
    # App/134/
    url(r'^(?P<restaurant_id>\d+)/$', views.detail, name='detail'),

]
