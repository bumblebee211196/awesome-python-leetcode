import pytest
from src._0026_remove_duplicates_from_sorted_array.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([1, 1, 2], 2),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
