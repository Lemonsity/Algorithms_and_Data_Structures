class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (p is None and q is not None) or (p is not None and q is None):
        return False
    if p is None and q is None:
        return True
    return p.val == q.val and \
        isSameTree(p.left, q.left) and \
        isSameTree(p.right, q.right)
