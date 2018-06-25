import pytest

from django.http import Http404
from django.test import RequestFactory

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

from .. import views


class TestIndexView:
    def test_anonymous(self):
        req = RequestFactory().get('/App/index')
        resp = views.index(req)

        assert resp.status_code == 200, 'should be callable by anyone'


class TestDetailViewWhenRaiseHttp404:
    def test_anonymous(self):
        req = RequestFactory().get('/App/detail/')
        with pytest.raises(Http404):
            views.detail(req, 6)


class TestDetailView:
    def test_anonymous(self):
        obj = mixer.blend('App.Restaurant')
        req = RequestFactory().get('/App/detail/')
        resp = views.detail(req, obj.pk)
        assert resp.status_code == 200, 'should be callable by anyone'
