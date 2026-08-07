class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k : int) -> int:
    def add_left(root, stack):
        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        stack.append(curr)

    stack = []
    add_left(root, stack)
    count, ans = 0, -1
    while count != k:
        top = stack.pop()
        if top is not None:
            count += 1
            ans = top.val
            add_left(top.right, stack)
    return ans
