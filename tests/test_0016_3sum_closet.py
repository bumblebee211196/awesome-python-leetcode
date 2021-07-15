import pytest
from src._0016_3sum_closet.solution import solution


class TestSolution:

    @pytest.mark.parametrize("nums, target, result", [
        ([-1,2,1,-4], 1, 2),
        ([-1,2,1,-4], 2, 2),
    ])
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
