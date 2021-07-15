import pytest
from src._0017_letter_combinations_of_a_phone_number.solution import solution

class TestSolution:

    @pytest.mark.parametrize("digits, result", [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("2", ["a","b","c"]),
        ("", []),
    ])
    def test_solution(self, digits, result):
        assert solution(digits) == result
