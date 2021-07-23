import pytest
from src._0042_trapping_rain_water.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, result",
        [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([1, 2], 0),
        ],
    )
    def test_solution(self, arr, result):
        assert solution(arr) == result
