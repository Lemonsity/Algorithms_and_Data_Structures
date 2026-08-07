class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end

def add_left(root, stack)
  curr = root
  while curr != nil do
    stack.append(curr)
    curr = curr.left
  end
  stack.append(curr)
end

def kth_smallest(root, k)
  stack = []
  add_left(root, stack)
  count = 0
  ans = -1
  while count != k do
    top = stack.pop()
    puts(top)
    if top != nil then
      count += 1
      ans = top.val
      add_left(top.right, stack)
    end
  end
  ans
end
