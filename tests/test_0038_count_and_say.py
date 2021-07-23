import pytest
from src._0038_count_and_say.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, result",
        [
            (1, "1"),
            (2, "11"),
            (4, "1211"),
        ],
    )
    def test_solution(self, nums, result):
        assert solution(nums) == result
