import pytest
from lib import fibonacci, bubble_sort, calculator

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []

def test_calculator():
    assert calculator(2, 3, "+") == 5
    with pytest.raises(ZeroDivisionError):
        calculator(1, 0, "/")
