import pytest
from src._0007_reverse_integer.solution import solution


class TestSolution:

    @pytest.mark.parametrize("x, result", [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (2147483649, 0)
    ])
    def test_solution(self, x, result):
        assert solution(x) == result
