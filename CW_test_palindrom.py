import pytest

from CW_palindrom import is_palindrom


def test_is_palindrom_true():
    assert is_palindrom('madam') == True

def test_is_palindrom_false():
    assert is_palindrom('madama') == False


@pytest.mark.parametrize('test_input, expected', [
    ('racecar', True),
    ('', True),
    ('level', True),
    ('lesson', False)
])
def test_is_palindrom(test_input, expected):
    assert is_palindrom(test_input) == expected
