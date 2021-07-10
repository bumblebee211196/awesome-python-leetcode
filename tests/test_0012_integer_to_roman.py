from src._0012_integer_to_roman.solution import solution

import pytest


class TestSolution:

    @pytest.mark.parametrize("num, result", [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ])
    def test_solution(self, num, result):
        assert solution(num) == result
