import pytest
from src._0040_combination_sum_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "candidates, target, result",
        [
            ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
            ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ],
    )
    def test_solution(self, candidates, target, result):
        assert solution(candidates, target) == result
