import pytest
from src._0079_word_search.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "board, word, result",
        [
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
        ],
    )
    def test_solution(self, board, word, result):
        assert solution(board, word) == result
