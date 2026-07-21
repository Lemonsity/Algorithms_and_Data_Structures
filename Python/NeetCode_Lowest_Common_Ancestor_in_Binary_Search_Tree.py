class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    root_val = root.val
    p_val = p.val
    q_val = q.val

    if (p_val < root_val and q_val < root_val):
        return lowestCommonAncestor(root.left, p, q)
    elif (root_val < p_val and root_val < q_val):
        return lowestCommonAncestor(root.right, p, q)
    return root
