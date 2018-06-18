# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    # succes = True

    app.login(username = "admin", password = "secret")
    app.create_group(Group(name="testgroup", header="testheader", footer="testfooter"))
    app.logout()
    # assertTrue(succes)

def test_failed(app):
    assert (1,2,3) == (1,2,3)
