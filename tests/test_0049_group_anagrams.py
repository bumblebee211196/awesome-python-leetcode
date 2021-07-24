import pytest
from src._0049_group_anagrams.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "strs, result",
        [
            (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
        ],
    )
    def test_solution(self, strs, result):
        assert solution(strs) == result
