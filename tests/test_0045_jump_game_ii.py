import pytest
from src._0045_jump_game_ii.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([2, 3, 1, 1, 4], 2),
            ([2, 3, 0, 1, 4], 2),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
