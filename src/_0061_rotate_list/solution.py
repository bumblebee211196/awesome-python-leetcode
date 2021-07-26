class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head
    curr = head
    n = 1
    while curr.next:
        n += 1
        curr = curr.next
    if k % n == 0:
        return head
    curr.next = head
    i = 1
    while i < n - (k % n):
        head = head.next
        i += 1
    curr = head.next
    head.next = None
    return curr
