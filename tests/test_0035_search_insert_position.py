import pytest
from src._0035_search_insert_position.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, target, result",
        [
            ([1, 3, 5, 6], 3, 1),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0),
            ([1], 0, 0),
        ],
    )
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
