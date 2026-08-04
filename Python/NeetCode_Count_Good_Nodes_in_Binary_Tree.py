from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    queue = deque([])
    queue.append( (root.val - 1, root) )

    count = 0
    while queue:
        (m, node) = queue.popleft()
        if m <= node.val:
            count += 1
        new_m = max(m, node.val)
        if node.left:
            queue.append( (new_m, node.left) )
        if node.right:
            queue.append( (new_m, node.right) )

    return count
