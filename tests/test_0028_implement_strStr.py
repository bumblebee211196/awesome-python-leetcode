import pytest
from src._0028_implement_strStr.solution import solution


class TestSolution:

    @pytest.mark.parametrize("haystack, needle, result", [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
    ])
    def test_solution(self, haystack, needle, result):
        assert solution(haystack, needle) == result
