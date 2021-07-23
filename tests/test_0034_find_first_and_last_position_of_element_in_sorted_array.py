import pytest
from src._0034_find_first_and_last_position_of_element_in_sorted_array.solution import (
    solution,
)


class TestSolution:
    @pytest.mark.parametrize(
        "nums, target, result",
        [
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 0, [-1, -1]),
        ],
    )
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
