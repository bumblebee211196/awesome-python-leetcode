import pytest
from src._0081_search_in_rotated_sorted_array_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, target, result",
        [
            ([2, 5, 6, 0, 0, 1, 2], 0, True),
            ([2, 5, 6, 0, 0, 1, 2], 3, False),
            ([4, 5, 6, 7, 0, 0, 2], 0, True),
            ([2, 5, 6, 7, 0, 1, 2], 2, True),
            ([5, 5, 6, 0, 1, 2, 3], 5, True),
        ],
    )
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
