import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestRestaurant:
    def test_model(self):
        obj = mixer.blend('App.Restaurant')
        assert obj.pk == 1, 'Should save an instance'

    def test_excerpt(self):
        obj = mixer.blend('App.Restaurant', name='Palm Beach')
        result = obj.get_excerpt(4)
        assert result == 'Palm', 'Should return some few characters'

    def test_str(self):
        obj = mixer.blend('App.Restaurant', name='Palm Beach')
        result = obj.__str__()
        assert result == 'Palm Beach', 'Should return a string as restaurant name'


class TestAddress:
    def test_model(self):
        obj = mixer.blend('App.Address')
        assert obj.pk == 1, 'Should save an instance'

    def test_str(self):
        obj = mixer.blend('App.Address', full_address='Noida Sector 137')
        result = obj.__str__()
        assert result == 'Noida Sector 137', 'Should return a string as full address'
