from collections import namedtuple
from assertpy import assert_that

Task = namedtuple('Task',['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defauls():
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert_that(t1 == t2).is_true()


def test_member_access():
    t = Task('by milk', 'Brian')
    assert_that(t.summary == 'by milk').is_true()
    assert_that(t.owner == 'Brian').is_true()
    assert_that((t.done, t.id) == (False, None)).is_true()