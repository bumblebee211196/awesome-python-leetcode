import pytest
from src._0001_two_sum.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, target, result",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ],
    )
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
