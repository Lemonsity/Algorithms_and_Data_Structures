from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBst(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    queue = deque([])
    queue.append( (-10000, 10000, root) )

    while queue:
        m, M, node = queue.popleft()
        if node.val <= m or M <= node.val:
            return False
        if node.left is not None:
            queue.append( (m, node.val, node.left) )
        if node.right is not None:
            queue.append( (node.val, M, node.right) )

    return True
