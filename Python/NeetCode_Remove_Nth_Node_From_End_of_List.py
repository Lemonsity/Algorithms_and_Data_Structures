class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    front = head
    back = head
    for i in range(n + 1):
        if front == None: # remove the head from the list
            return head.next
        front = front.next

    while front != None:
        front = front.next
        back = back.next

    back.next = back.next.next
    return head
