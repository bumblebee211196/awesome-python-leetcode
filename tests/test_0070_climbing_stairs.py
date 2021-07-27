import pytest
from src._0070_climbing_stairs.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, result",
        [
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 8),
        ],
    )
    def test_solution(self, n, result):
        assert solution(n) == result
