import pytest
from src._0009_pallindrome_number.solution import solution


class TestSolution:

    @pytest.mark.parametrize("x, result", [
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
    ])
    def test_solution(self, x, result):
        assert solution(x) == result
