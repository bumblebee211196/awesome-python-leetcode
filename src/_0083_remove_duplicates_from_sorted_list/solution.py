class ListNode:
    def __init__(self, x, next_=None):
        self.val = x
        self.next = next_


def solution(head: ListNode) -> ListNode:
    prev = head
    curr = head
    while curr:
        if prev.val == curr.val:
            curr = curr.next
        else:
            prev.next = curr
            prev = curr
            curr = curr.next
    if prev:
        prev.next = None
    return head
