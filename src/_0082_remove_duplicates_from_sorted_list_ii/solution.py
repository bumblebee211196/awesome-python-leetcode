from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(head: Optional[ListNode]) -> Optional[ListNode]:
    seen = set()
    to_remove = set()
    curr = head
    while curr:
        if curr.val not in seen:
            seen.add(curr.val)
        else:
            to_remove.add(curr.val)
        curr = curr.next
    dummy = ListNode(-999)
    p1, p2 = dummy, head
    p2_next = None
    while p2:
        p2_next = p2.next
        p2.next = None
        if p2.val not in to_remove:
            p1.next = p2
            p1 = p1.next
        p2 = p2_next
    return dummy.next
