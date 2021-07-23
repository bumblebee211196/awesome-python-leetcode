import pytest
from src._0039_combination_sum.solution import solution

class TestSolution:

    @pytest.mark.parametrize("candidates, target, result", [
        ([2,3,6,7], 7, [[2, 2, 3], [7]]),
        ([2,3,5], 8, [[2,2,2,2], [2,3,3], [3,5]]),
        ([2], 1, []),
        ([1], 1, [[1]]),
        ([1], 2, [[1,1]]),
    ])
    def test_solution(self, candidates, target, result):
        assert solution(candidates, target) == result
