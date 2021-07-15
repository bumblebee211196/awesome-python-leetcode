class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def solution(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        res = l1
        res.next = solution(l1.next, l2)
    else:
        res = l2
        res.next = solution(l1, l2.next)
    return res
