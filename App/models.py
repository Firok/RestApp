from django.db import models


class Address(models.Model):
    full_address = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    street_code = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_address


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.name
