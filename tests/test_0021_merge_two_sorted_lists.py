from typing import List
import pytest
from src._0021_merge_two_sorted_lists.solution import ListNode, solution


class TestSolution:

    @pytest.mark.parametrize("l1, l2, result", [
        (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))), 
        ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))),
        (None, None, None),
        (None, ListNode(0), ListNode(0)),
        (ListNode(0), None, ListNode(0)),
    ])
    def test_solution(self, l1, l2, result):
        assert self.is_equal(solution(l1, l2), result)

    def is_equal(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
