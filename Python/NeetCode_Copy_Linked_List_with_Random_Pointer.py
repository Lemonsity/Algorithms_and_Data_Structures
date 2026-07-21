class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if head == None:
        return None

    index = 0
    node_to_index = dict()
    index_to_val = []

    node = head
    while node:
        node_to_index[node] = index
        index_to_val.append(node.val)
        node = node.next
        index += 1

    length = index
    graph = []
    node = head
    for i in range(length):
        random_node = node.random
        if (random_node != None):
            graph.append((i, node_to_index[random_node]))
        node = node.next

    results = [Node(index_to_val[i]) for i in range(length)]
    for i in range(length - 1):
        results[i].next = results[i + 1]

    for (src, tgt) in graph:
        results[src].random = results[tgt]

    return results[0]
