import pytest
from src._0080_remove_duplicates_from_sorted_array_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([1, 1, 1, 2, 2, 3], 5),
            ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
