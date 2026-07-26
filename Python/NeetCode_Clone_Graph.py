from collections import deque, defaultdict


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if node is None:
        return None

    copies = dict()
    queue = deque([])
    queue.append(node)

    while queue:
        top = queue.popleft()
        if top not in copies:
            copies[top] = Node(top.val)

        for neighbor in top.neighbors:
            if neighbor not in copies:
                copies[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            copies[top].neighbors.append(copies[neighbor])

    return copies[node]


def cloneGraph_(node: Optional['Node']) -> Optional['Node']:
    if node is None:
        return None

    copies = defaultdict(Node)
    queue = deque([])
    visited = set()

    queue.append(node)

    while queue:
        top = queue.popleft()

        """ Why is the following check necessary:
        Consider the following case:
          1
         / \
        2 - 3
        Assume the initial node is 1
        Without the following check, we will add 3 into the queue twice
        One from adding the neighbours of 1
        One from adding the neighbours of 2
        Then the later append will added 3's neighbour twice as a result
        """
        if top in visited:
            continue

        visited.add(top)

        copies[top].val = top.val

        for neighbor in top.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
            copies[top].neighbors.append(copies[neighbor])

    return copies[node]
