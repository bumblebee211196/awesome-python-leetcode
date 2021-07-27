import pytest
from src._0066_plus_one.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "digits, result", [([1, 2, 3], [1, 2, 4]), ([9, 9], [1, 0, 0]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([0], [1])]
    )
    def test_solution(self, digits, result):
        assert solution(digits) == result
