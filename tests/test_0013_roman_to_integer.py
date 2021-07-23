import pytest
from src._0013_roman_to_integer.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, result",
        [
            ("III", 3),
            ("IV", 4),
            ("IX", 9),
            ("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
        ],
    )
    def test_solution(self, s, result):
        assert solution(s) == result
