import pytest
from src._0014_longest_common_prefix.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "strs, result",
        [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            ([], ""),
            (["cat"], "cat"),
        ],
    )
    def test_solution(self, strs, result):
        assert solution(strs) == result
