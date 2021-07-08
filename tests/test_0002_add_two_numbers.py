from typing import List
from src._0002_add_two_numbers.solution import solution, ListNode

import pytest


class TestSolution:

    @pytest.mark.parametrize("l1, l2, result", [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
        ([1, 2], [3, 4, 5, 6, 7], [4, 6, 5, 6, 7])
    ])
    def test_solution(self, l1, l2, result):
        assert self.listnode_to_list(solution(self.list_to_listnode(l1), self.list_to_listnode(l2))) == result

    def list_to_listnode(self, nums: List[int]) -> ListNode:
        head = curr = ListNode(-1)
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    def listnode_to_list(self, head: ListNode) -> List[int]:
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        return nums
