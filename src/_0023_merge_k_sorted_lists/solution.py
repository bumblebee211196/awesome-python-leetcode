import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(lists: List[ListNode]) -> ListNode:
    n = len(lists)
    heap = []
    for i in range(n):
        curr = lists[i]
        while curr:
            heapq.heappush(heap, curr.val)
            curr = curr.next
    head = ListNode(-1)
    curr = head
    while heap:
        curr.next = ListNode(heapq.heappop(heap))
        curr = curr.next
    return head.next
    