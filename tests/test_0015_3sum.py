from src._0015_3sum.solution import solution

import pytest


class TestSolution:

    @pytest.mark.parametrize("nums, result", [
        ([3,7,11,87,9,-9,19,-18], [[-18,7,11]]),
        ([2,2,3,7,7,87,9,9,19,19,9,-9,19,-18,], [[-18,9,9],[-9,2,7]]),
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([1,2,-3], [[-3,1,2]]),
        ([1,2], []),
        ([0], []),
    ])
    def test_solution(self, nums, result):
        assert solution(nums) == result
