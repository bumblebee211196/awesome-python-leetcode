import pytest
from src._0003_longest_substring_without_repeating_characters.solution import solution


class TestSolution:
    @pytest.mark.parametrize("s, result", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0)])
    def test_solution(self, s, result):
        assert solution(s) == result
