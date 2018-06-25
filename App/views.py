from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Restaurant, Address
from .serializers import AddressSerializer, RestaurantSerializer


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


def index(request):
    all_restaurants = Restaurant.objects.all()
    context = {
        'all_restaurants': all_restaurants
    }
    return render(request, 'App/index.html', context)


def detail(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    return render(request, 'App/detail.html', {'restaurant': restaurant})
