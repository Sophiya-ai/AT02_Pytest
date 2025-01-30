import pytest

from CW_arithm_ab import add, subtract


def test_add2():
    assert add(1, 1) == 2


def test_sub2():
    assert subtract(10, 1) == 1
