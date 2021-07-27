import pytest
from src._0063_unique_paths_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "obstacle_grid, result",
        [
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
            ([[0, 1], [0, 0]], 1),
            ([[1, 1], [0, 0]], 0),
        ],
    )
    def test_solution(self, obstacle_grid, result):
        assert solution(obstacle_grid) == result
