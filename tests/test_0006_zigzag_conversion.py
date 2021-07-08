from src._0006_zigzag_conversion.solution import solution

import pytest


class TestSolution:

    @pytest.mark.parametrize("s, numRows, result", [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ])
    def test_solution(self, s, numRows, result):
        assert solution(s, numRows) == result
