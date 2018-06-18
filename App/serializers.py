from rest_framework import serializers

from .models import Restaurant, Address


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'phone', 'address')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'full_address', 'street', 'street_code', 'pincode', 'city', 'country')
