class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    head.val, head.next.val = head.next.val, head.val
    solution(head.next.next)
    return head
