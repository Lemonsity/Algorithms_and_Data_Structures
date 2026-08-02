def isValid(s: str) -> bool:
    open_p = [ '(', '[', '{' ]
    close_p = [ ')', ']', '}' ]
    pairs = [ ('(', ')'), ('[', ']'), ('{', '}') ]

    stack = []
    for c in s:
        if c in open_p:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            top = stack[-1]
            if (top, c) in pairs:
                stack.pop()
            else:
                return False
    return len(stack) == 0
