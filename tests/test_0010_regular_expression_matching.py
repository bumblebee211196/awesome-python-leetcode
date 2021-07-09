from src._0010_regular_expression_matching.solution import solution

import pytest


class TestSolution:

    @pytest.mark.parametrize("s, p, result", [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ])
    def test_solution(self, s, p, result):
        assert solution(s, p) == result
