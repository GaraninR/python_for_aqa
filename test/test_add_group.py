# -*- coding: utf-8 -*-
import time

from model.group import Group


def test_add_group(app):
    # succes = True
    app.group.create(Group(name="testgroup", header="testheader", footer="testfooter"))
    # assertTrue(succes)

def test_passed_example(app):
    assert (1,2,3) == (1,2,3)

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
