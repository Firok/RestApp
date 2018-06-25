from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('addresses', views.AddressView)
router.register('restaurants', views.RestaurantView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'index', views.index, name='index'),
    # App/134/
    url(r'detail/(?P<restaurant_id>\d+)/', views.detail, name='detail'),

]
