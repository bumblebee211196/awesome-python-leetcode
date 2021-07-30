import pytest
from src._0077_combinations.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, k, result",
        [
            (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
            (1, 1, [[1]]),
        ],
    )
    def test_solution(self, n, k, result):
        assert solution(n, k) == result
