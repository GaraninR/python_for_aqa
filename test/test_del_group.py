from model.group import Group
from assertpy import *


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert_that(len(old_groups) - 1 == len(new_groups)).is_true()

    old_groups[0:1] = []
    # assert (old_groups == new_groups)
    assert_that(old_groups == new_groups)