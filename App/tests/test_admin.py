import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

from .. import admin
from .. import models

pytestmark = pytest.mark.django_db

class TestRestaurantAdmin:

    def test_excerpt(self):
        site = AdminSite()
        restaurant_admin = admin.RestaurantAdmin(models.Restaurant, site)
        obj = mixer.blend('App.Restaurant', name='Palm Beach')
        result = restaurant_admin.excerpt(obj)
        assert result == 'Palm', 'Should return some few characters'