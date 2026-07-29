class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def clean_up(l: Optional[ListNode]) -> Optional[ListNode]:
        if l is not None and l.val == 0:
            return None
        return l

    def closer(l: Optional[ListNode], carry: bool) -> Optional[ListNode]:
        if not carry:
            return l

        if l is None:
            return ListNode(1, None)

        if l.val < 9:
            l.val += 1
            return l
        l.next = closer(l.next, True)
        l.val = 0
        return l

    def aux(l1, l2, carry):
        if l1 is None:
            return closer(l2, carry)
        if l2 is None:
            return closer(l1, carry)
        new_val = l1.val + l2.val + (1 if carry else 0)
        new_node = ListNode(new_val % 10)
        new_node.next = aux(l1.next, l2.next, new_val >= 10)
        return new_node

    l1 = clean_up(l1)
    l2 = clean_up(l2)
    ans = aux(l1, l2, False)
    return ans if ans is not None else ListNode(0, None)
