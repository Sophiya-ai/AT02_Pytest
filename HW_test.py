import pytest

from HW import count_vowel


@pytest.mark.parametrize('input_string, expected', [
    ('aaauuuooёииии', 13),
    ('gggttt pt вввв', 0),
    ('A lot of things ArE NOT usFULL', 9)
])
def test_count_vowel(input_string, expected):
    assert count_vowel(input_string) == expected
