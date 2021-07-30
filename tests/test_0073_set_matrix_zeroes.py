import pytest
from src._0073_set_matrix_zeroes.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, result",
        [
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
            ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        ],
    )
    def test_solution(self, matrix, result):
        solution(matrix)
        assert matrix == result
