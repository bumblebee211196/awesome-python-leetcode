import pytest
from src._0008_string_to_integer_atoi.solution import solution


class TestSolution:

    @pytest.mark.parametrize("s, result", [
        ("42", 42),
        (" +42 ", 42),
        ("    -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("91283472332 hello", 2147483647)
    ])
    def test_solution(self, s, result):
        assert solution(s) == result
