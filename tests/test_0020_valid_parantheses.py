import pytest
from src._0020_valid_parantheses.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, result",
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([)]", False),
            ("{[]}", True),
        ],
    )
    def test_solution(self, s, result):
        assert solution(s) == result
