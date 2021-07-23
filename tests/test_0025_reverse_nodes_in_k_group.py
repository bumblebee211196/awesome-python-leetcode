import pytest
from src._0025_reverse_nodes_in_k_group.solution import ListNode, solution


class TestSolution:
    @pytest.mark.parametrize(
        "head, k, result",
        [
            (
                (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))),
                2,
                ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5))))),
            ),
            (
                (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))),
                3,
                ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))),
            ),
            (
                (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))),
                1,
                ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ),
            (ListNode(1), 1, ListNode(1)),
        ],
    )
    def test_solution(self, head, k, result):
        assert self.is_equal(solution(head, k), result)

    def is_equal(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
