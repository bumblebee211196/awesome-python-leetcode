import pytest
from src._0056_merge_intervals.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "intervals, result",
        [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[1, 4], [2, 3]], [[1, 4]]),
            ([[1, 4]], [[1, 4]]),
        ],
    )
    def test_solution(self, intervals, result):
        assert solution(intervals) == result
