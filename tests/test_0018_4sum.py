import pytest
from src._0018_4sum.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, target, result",
        [
            ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
            ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ],
    )
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
