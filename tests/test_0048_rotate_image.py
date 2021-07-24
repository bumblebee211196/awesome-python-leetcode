import pytest
from src._0048_rotate_image.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, result",
        [
            ([[1]], [[1]]),
            ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            (
                [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            ),
        ],
    )
    def test_solution(self, matrix, result):
        solution(matrix)
        assert matrix == result
