import pytest
from src._0088_merge_sorted_array.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums1, m, nums2, n, result",
        [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1]),
        ],
    )
    def test_solution(self, nums1, m, nums2, n, result):
        solution(nums1, m, nums2, n)
        assert nums1 == result
