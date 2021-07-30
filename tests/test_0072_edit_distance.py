import pytest
from src._0072_edit_distance.solution import solution1, solution2


class TestSolution:
    @pytest.mark.parametrize(
        "word1, word2, result",
        [
            ("horse", "ros", 3),
            ("intention", "execution", 5),
        ],
    )
    def test_solution(self, word1, word2, result):
        assert solution1(word1, word2) == result
        assert solution2(word1, word2) == result
