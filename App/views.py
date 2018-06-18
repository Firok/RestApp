from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Restaurant, Address
from .serializers import RestaurantSerializer, AddressSerializer


@api_view(['GET', 'POST'])
def restaurant_api(request):
    """
    List all restaurants or create a new restaurant record.
    """
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def address_api(request):
    """
    List all address or create a new address record.
    """
    if request.method == 'GET':
        address_list = Address.objects.all()
        serializer = AddressSerializer(address_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
