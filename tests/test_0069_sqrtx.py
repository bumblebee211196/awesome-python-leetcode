import pytest
from src._0069_sqrtx.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "x, result",
        [
            (4, 2),
            (1, 1),
            (8, 2),
        ],
    )
    def test_solution(self, x, result):
        assert solution(x) == result
