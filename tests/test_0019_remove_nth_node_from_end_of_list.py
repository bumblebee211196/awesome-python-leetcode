import pytest
from src._0019_remove_nth_node_from_end_of_list.solution import solution, ListNode


class TestSolution:

    @pytest.mark.parametrize("head, n, result", [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, ListNode(1, ListNode(2, ListNode(3, ListNode(4))))),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, ListNode(1, ListNode(2, ListNode(3, ListNode(5))))),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3, ListNode(1, ListNode(2, ListNode(4, ListNode(5))))),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 4, ListNode(1, ListNode(3, ListNode(4, ListNode(5))))),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        (ListNode(1), 1, None),
        (ListNode(1, ListNode(2)), 1, ListNode(1)),
    ])
    def test_solution(self, head, n, result):
        assert self.is_equal(solution(head, n), result)

    def is_equal(self, head1, head2):
        c1, c2 = head1, head2
        while c1 and c2:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next
        return True
