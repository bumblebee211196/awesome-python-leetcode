import pytest
from src._0004_median_of_two_sorted_arrays.solution import solution


class TestSolution:

    @pytest.mark.parametrize("nums1, nums2, result", [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ])
    def test_solution(self, nums1, nums2, result):
        assert solution(nums1, nums2) == result
