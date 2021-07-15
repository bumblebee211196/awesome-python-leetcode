import pytest
from src._0022_generate_parantheses.solution import solution


class TestSolution:

    @pytest.mark.parametrize("n, result", [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"]),
    ])
    def test_solution(self, n, result):
        assert solution(n) == result
