import pytest
from src._0057_insert_interval.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "intervals, new_interval, result",
        [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([], [5, 7], [[5, 7]]),
            ([[1, 5]], [2, 3], [[1, 5]]),
            ([[1, 5]], [2, 7], [[1, 7]]),
        ],
    )
    def test_solution(self, intervals, new_interval, result):
        assert solution(intervals, new_interval) == result
