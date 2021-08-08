from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    left = ListNode(-999)
    right = ListNode(-999)
    l, r, curr = left, right, head
    while curr:
        if curr.val < x:
            l.next = ListNode(curr.val)
            l = l.next
        else:
            r.next = ListNode(curr.val)
            r = r.next
        curr = curr.next
    left, right = left.next, right.next
    l.next = right
    return left if left else right
