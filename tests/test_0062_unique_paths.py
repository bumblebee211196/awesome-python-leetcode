import pytest
from src._0062_unique_paths.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "m, n, result",
        [
            (3, 7, 28),
            (3, 2, 3),
            (7, 3, 28),
            (3, 3, 6),
        ],
    )
    def test_solution(self, m, n, result):
        assert solution(m, n) == result
