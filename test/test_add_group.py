# -*- coding: utf-8 -*-
import time
from assertpy import *

from model.group import Group


def test_add_group(app):
    # succes = True
    old_groups = app.group.get_group_list()
    group = Group(name="testgroup", header="testheader", footer="testfooter")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert_that(len(old_groups) + 1 == len(new_groups)).is_true()
    # assertTrue(succes)
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    assert_that(old_groups == new_groups)

def test_passed_example(app):
    assert (1,2,3) == (1,2,3)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert_that(len(old_groups) + 1 == len(new_groups)).is_true()
    assert_that(old_groups == new_groups)
