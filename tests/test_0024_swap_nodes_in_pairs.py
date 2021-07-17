from typing import List
import pytest
from src._0024_swap_nodes_in_pairs.solution import ListNode, solution


class TestSolution:

    @pytest.mark.parametrize("nums, result", [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), ListNode(2, ListNode(1, ListNode(4, ListNode(3))))),
        (ListNode(1), ListNode(1)),
        (None, None),
    ])
    def test_solution(self, nums, result):
        assert self.is_equal(solution(nums), result)

    def is_equal(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
