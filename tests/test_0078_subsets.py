import pytest
from src._0078_subsets.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
            ([0], [[], [0]]),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
