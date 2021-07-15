import pytest
from src._0011_container_with_most_water.solution import solution


class TestSolution:

    @pytest.mark.parametrize("height, result", [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([4,3,2,1,4], 16),
        ([1,2,1], 2),
    ])
    def test_solution(self, height, result):
        assert solution(height) == result
