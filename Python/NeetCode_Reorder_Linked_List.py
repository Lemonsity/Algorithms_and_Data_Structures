class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    if head == None:
        return

    nodes = []
    node = head
    while node != None:
        nodes.append(node)
        node = node.next

    last_node = nodes[0]
    i, j = 0, len(nodes) - 1
    while i <= j:
        if (i == j):
            nodes[i].next = None
            break

        nodes[i].next = nodes[j]
        nodes[j].next = None

        i += 1
        if (i < j):
            nodes[j].next = nodes[i]
        j -= 1

    return
