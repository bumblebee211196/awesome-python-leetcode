import pytest
from src._0027_remove_element.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, val, result",
        [
            ([3, 2, 2, 3], 3, 2),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ],
    )
    def test_solution(self, nums, val, result):
        assert solution(nums, val) == result
