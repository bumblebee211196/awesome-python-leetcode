import pytest
from src._0059_spiral_matrix_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, result",
        [
            (1, [[1]]),
            (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        ],
    )
    def test_solution(self, n, result):
        assert solution(n) == result
