import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    queue = deque([])
    ans = []
    queue.append((root, 0))

    while queue:
        (node, height) = queue.popleft()
        if len(ans) == height:
            ans.append(node.val)
        else:
            ans[height] = node.val

        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))
    return ans
