from rest_framework import serializers

from .models import Restaurant, Address


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'url', 'name', 'phone', 'address')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'url', 'full_address', 'street', 'street_code', 'pincode', 'city', 'country')
