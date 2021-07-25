import pytest
from src._0055_jump_game.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
