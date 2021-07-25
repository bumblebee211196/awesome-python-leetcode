import pytest
from src._0053_maximum_subarray.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
