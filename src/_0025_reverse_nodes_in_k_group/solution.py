class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k <= 1:
        return head
    dummy = ListNode(-1)
    prev = dummy
    ptr, c = head, 0
    while ptr:
        c += 1
        if c % k == 0:
            next_ = ptr.next
            ptr.next = None
            r_head = reverse(head)
            head.next, ptr = next_, next_
            prev.next = r_head
            prev = head
            head = head.next
        else:
            ptr = ptr.next
    return dummy.next

def reverse(head: ListNode) -> ListNode:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
