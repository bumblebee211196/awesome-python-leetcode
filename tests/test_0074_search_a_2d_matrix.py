import pytest
from src._0074_search_a_2d_matrix.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, target, result",
        [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ],
    )
    def test_solution(self, matrix, target, result):
        assert solution(matrix, target) == result
