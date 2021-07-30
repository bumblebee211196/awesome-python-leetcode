import pytest
from src._0071_simplify_path.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "path, result",
        [
            ("/home/", "/home"),
            ("/../", "/"),
            ("/home//foo/", "/home/foo"),
            ("/a/./b/../../c/", "/c"),
        ],
    )
    def test_solution(self, path, result):
        assert solution(path) == result
