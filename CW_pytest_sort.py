import pytest

from CW_sort import sort_list


def test_sort1():
    assert sort_list([3, 6, 1, 2, 2, 8]) == [1, 2, 2, 3, 6, 8]


def test_sort2():
    assert sort_list([-3, 6, 1, -2, 2, 8]) == [-3, -2, 1, 2, 6, 8]



