import pytest
from src._0058_length_of_last_word.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, result",
        [
            ("Hello World", 5),
            (" ", 0),
        ],
    )
    def test_solution(self, s, result):
        assert solution(s) == result
