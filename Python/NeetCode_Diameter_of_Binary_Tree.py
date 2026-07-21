class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root: Optional[TreeNode]) -> tuple(int, int):
    if root == None:
        return (0, 0)
    (left_diameter, left_depth) = helper(root.left)
    (right_diameter, right_depth) = helper(root.right)
    max_diameter = max([left_diameter, right_diameter, left_depth + right_depth + 2)])
    max_depth = 1 + max(left_depth, right_depth)
    return (max_diameter, max_depth)

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    (diameter, _) = helper(root)
    return diameter
