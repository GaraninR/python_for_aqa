from model.group import Group
from assertpy import *


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert_that(len(old_groups) == len(new_groups)).is_true()


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert_that(len(old_groups) == len(new_groups)).is_true()
