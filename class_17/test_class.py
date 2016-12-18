# -*- coding: utf-8 -*-
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def f():
    raise SystemExit(1)


# @pytest.mark.xfail(SystemExit)
def test_exception():
    with pytest.raises(SystemExit):
        f()


class TestClass(object):

    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')


@pytest.fixture()
def before():
    print ('\nbefore each test')


@pytest.mark.usefixtures('before')
class Test2(object):

    def test_1(before):
        print('test_1()')

    def test_2(before):
        print 'test_2()'

    def test_3(self):
        print 'test_3()'


@pytest.fixture
def some_data():
    a = 'before'
    yield {1: 'one', 'foo': 'bar'}
    print 'yield'


def test_data(some_data):
    assert some_data['foo'] == 'bar'
# if __name__ == '__main__':
#     test_answer()
