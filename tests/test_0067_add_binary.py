import pytest
from src._0067_add_binary.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "a, b, result",
        [
            ("11", "1", "100"),
            ("1", "11", "100"),
            ("1010", "1011", "10101"),
        ],
    )
    def test_solution(self, a, b, result):
        assert solution(a, b) == result
