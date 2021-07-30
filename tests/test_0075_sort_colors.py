import pytest
from src._0075_sort_colors.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 0, 1], [0, 1, 2]),
            ([0], [0]),
            ([1], [1]),
        ],
    )
    def test_solution(self, nums, result):
        solution(nums)
        assert nums == result
