class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    if head == None:
        return False
    n1 = head
    n2 = head.next
    while True:
        if (n1 == n2):
            return True
        elif (n2 == None):
            return False
        else:
            n2 = n2.next
            if (n2 == None):
                return False
            n2 = n2.next
            n1 = n1.next
    return False
