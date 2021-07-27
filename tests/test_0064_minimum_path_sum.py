import pytest
from src._0064_minimum_path_sum.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "grid, result",
        [
            ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
            ([[1, 2, 3], [4, 5, 6]], 12),
        ],
    )
    def test_solution(self, grid, result):
        assert solution(grid) == result
