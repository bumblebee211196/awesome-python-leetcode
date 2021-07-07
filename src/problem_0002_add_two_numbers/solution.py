# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        c1, c2 = l1, l2
        res = c3 = ListNode(-1)
        while c1 and c2:
            carry, r = divmod(c1.val + c2.val + carry, 10)
            c3.next = ListNode(r)
            c1 = c1.next
            c2 = c2.next
            c3 = c3.next
        while c1:
            carry, r = divmod(c1.val + carry, 10)
            c3.next = ListNode(r)
            c1 = c1.next
            c3 = c3.next
        while c2:
            carry, r = divmod(c2.val + carry, 10)
            c3.next = ListNode(r)
            c2 = c2.next
            c3 = c3.next
        if carry > 0:
            c3.next = ListNode(carry)
        return res.next