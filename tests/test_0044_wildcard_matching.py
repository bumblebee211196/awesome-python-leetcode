import pytest
from src._0044_wildcard_matching.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, p, result",
        [
            ("aa", "a", False),
            ("aa", "*", True),
            ("cb", "?a", False),
            ("adceb", "*a*b", True),
            ("acdcb", "a*c?b", False),
        ],
    )
    def test_solution(self, s, p, result):
        assert solution(s, p) == result
