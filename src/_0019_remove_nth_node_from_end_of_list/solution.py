class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(head: ListNode, n: int) -> ListNode:
    curr = head
    for _ in range(n):
        curr = curr.next
    first, second = head, curr
    if not second:
        return first.next
    while second.next:
        first = first.next
        second = second.next
    first.next = first.next.next
    return head
