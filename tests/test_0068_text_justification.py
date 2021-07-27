import pytest
from src._0068_text_justification.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "words, k, result",
        [
            (
                ["This", "is", "an", "example", "of", "text", "justification."],
                16,
                ["This    is    an", "example  of text", "justification.  "],
            ),
            (
                ["What", "must", "be", "acknowledgment", "shall", "be"],
                16,
                ["What   must   be", "acknowledgment  ", "shall be        "],
            ),
            (
                [
                    "Science",
                    "is",
                    "what",
                    "we",
                    "understand",
                    "well",
                    "enough",
                    "to",
                    "explain",
                    "to",
                    "a",
                    "computer.",
                    "Art",
                    "is",
                    "everything",
                    "else",
                    "we",
                    "do",
                ],
                20,
                [
                    "Science  is  what we",
                    "understand      well",
                    "enough to explain to",
                    "a  computer.  Art is",
                    "everything  else  we",
                    "do                  ",
                ],
            ),
        ],
    )
    def test_solution(self, words, k, result):
        assert solution(words, k) == result
