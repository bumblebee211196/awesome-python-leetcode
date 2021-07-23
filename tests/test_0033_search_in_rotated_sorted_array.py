import pytest
from src._0033_search_in_rotated_sorted_array.solution import solution


class TestSolution:

    @pytest.mark.parametrize("nums, target, result", [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 2, 6),
        ([4,5,6,0,1,2,3], 5, 1),
        ([4,5,6,0,1,2,3], 2, 5),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
    ])
    def test_solution(self, nums, target, result):
        assert solution(nums, target) == result
