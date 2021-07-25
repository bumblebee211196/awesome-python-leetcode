import pytest
from src._0054_spiral_matrix.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, result",
        [
            ([], []),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ],
    )
    def test_solution(self, matrix, result):
        assert solution(matrix) == result
