from src._0005_longest_pallindromic_substring.solution import solution

import pytest


class TestSolution:

    @pytest.mark.parametrize("s, result", [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
    ])
    def test_solution(self, s, result):
        assert solution(s) in result