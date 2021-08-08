from typing import List
import pytest
from src._0082_remove_duplicates_from_sorted_list_ii.solution import solution, ListNode


class TestSolution:
    @pytest.mark.parametrize(
        "head, result",
        [
            (
                ListNode(1, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))),
                ListNode(1, ListNode(5)),
            ),
            (ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))), ListNode(2, ListNode(3))),
        ],
    )
    def test_solution(self, head, result):
        assert self.is_equal(solution(head), result)

    def is_equal(self, head1, head2):
        c1, c2 = head1, head2
        while c1 and c2:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next
        return True
