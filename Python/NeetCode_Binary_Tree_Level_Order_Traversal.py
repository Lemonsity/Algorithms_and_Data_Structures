class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root == None:
        return []

    ans = []
    cur_level = [root]
    next_level = []

    while len(cur_level) != 0:
        level = []
        for node in cur_level:
            level.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        ans.append(level)
        cur_level = next_level
        next_level = []

    return ans
