import pytest
from src._0023_merge_k_sorted_lists.solution import ListNode, solution


class TestSolution:

    @pytest.mark.parametrize("lists, result", [
        (
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
                ListNode(2, ListNode(6)),
            ],
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
        ),
        (
            [],
            []
        ),
        (
            [[]],
            []
        )
    ])
    def test_solution(self, lists, result):
        assert self.is_equal(solution(lists), result)

    def is_equal(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
