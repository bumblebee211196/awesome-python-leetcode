import pytest
from src._0086_partition_list.solution import ListNode, solution


class TestSolution:
    @pytest.mark.parametrize(
        "head, x, result",
        [
            (
                ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))),
                3,
                ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(3, ListNode(5)))))),
            ),
            (ListNode(2, ListNode(1)), 2, ListNode(1, ListNode(2))),
            (ListNode(1), 0, ListNode(1)),
        ],
    )
    def test_solution(self, head, x, result):
        assert self.is_equal(solution(head, x), result)

    def is_equal(self, head1, head2):
        c1, c2 = head1, head2
        while c1 and c2:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next
        return True
