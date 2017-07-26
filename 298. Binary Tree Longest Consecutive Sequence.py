if not root:
        return 0
        
    ret = 0
    stack = [(root, 1)]
    while stack:
        node, cnt = stack.pop()
        if node.left:
            stack.append((node.left, cnt+1 if node.left.val == node.val + 1 else 1))
        if node.right:
            stack.append((node.right, cnt+1 if node.right.val == node.val + 1 else 1))
        ret = max(ret, cnt)
        
    return ret