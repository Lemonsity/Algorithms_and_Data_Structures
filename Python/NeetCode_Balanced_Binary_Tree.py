class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(root):
    if root == None:
        return (0, true)

    (left_height, left_balanced) = helper(root.left)
    (right_height, right_balanced) = helper(root.right)
    return (1 + max(left_height, right_height), \
            left_balanced and right_balanced and math.abs(left_height - right_height) <= 1)

def isBalanced(root: Optional[TreeNode]) -> bool:
    (_, is_balanced) = helper(root)
    return is_balanced
