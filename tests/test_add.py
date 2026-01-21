from src.add import add
import pytest

def test_happy_path() -> None:
    assert add(2,3) == 5

def test_case1() -> None:
    assert add(-3, 4) == 1

def test_case_two_negs() -> None:
    assert add(-3, -4) == -7

def test_floats() -> None:
    assert add(3.0, 4.3) == 7.3

@pytest.mark.parametrize(
    "input1, input2, expected",
    [(2, 3, 5), (-3, 4, 1), (-3, -4, -7), (3.0, 4.3, 7.3)],
)
def test_add(input1, input2, expected):
    assert add(input1, input2) == expected
