import pytest
from src._0043_multiply_strings.solution import solution


class TestSolution:

    @pytest.mark.parametrize("num1, num2, result", [
        ("1", "0", "0"),
        ("2", "3", "6"),
        ("123", "456", "56088"),
        ("99999", "99999", "9999800001"),
    ])
    def test_solution(self, num1, num2, result):
        assert solution(num1, num2) == result
