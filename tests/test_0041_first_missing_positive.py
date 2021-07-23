import pytest
from src._0041_first_missing_positive.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
