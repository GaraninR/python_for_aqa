# -*- coding: utf-8 -*-
import time
from assertpy import *

from model.group import Group


def test_add_group(app):
    # succes = True
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="testgroup", header="testheader", footer="testfooter"))
    new_groups = app.group.get_group_list()
    assert_that(len(old_groups) + 1 == len(new_groups)).is_true()
    # assertTrue(succes)

def test_passed_example(app):
    assert (1,2,3) == (1,2,3)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert_that(len(old_groups) + 1 == len(new_groups)).is_true()
