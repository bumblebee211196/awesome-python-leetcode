import pytest
from src._0052_n_queens_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, result",
        [
            (4, 2),
            (1, 1),
        ],
    )
    def test_solution(self, n, result):
        assert solution(n) == result
