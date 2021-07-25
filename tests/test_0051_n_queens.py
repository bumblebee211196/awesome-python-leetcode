import pytest
from src._0051_n_queens.solution import solution1, solution2


class TestSolution:
    @pytest.mark.parametrize(
        "n, result",
        [
            (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
            (1, [["Q"]]),
        ],
    )
    def test_solution(self, n, result):
        assert solution1(n) == result
        assert solution2(n) == result
