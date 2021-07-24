import pytest
from src._0047_permutations_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
