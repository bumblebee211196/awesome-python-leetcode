import pytest
from src._0050_powx_n.solution import solution


class TestSolution:

    @pytest.mark.parametrize("x, n, result", [
        (2.0, -2, 0.25),
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261000000000001),
    ])
    def test_solution(self, x, n, result):
        assert solution(x, n) == result
