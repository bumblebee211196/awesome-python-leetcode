import pytest
from src._0029_divide_two_integers.solution import solution


class TestSolution:

    @pytest.mark.parametrize("dividend, divisor, result", [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
    ])
    def test_solution(self, dividend, divisor, result):
        assert solution(dividend, divisor) == result
