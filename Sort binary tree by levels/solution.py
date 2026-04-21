from collections import deque

def tree_by_levels(node):
    
    if node is None:
        return []
    
    result = []
    
    queue = deque([node])
    
    while queue:
        first = queue.popleft()
        result.append(first.value)

        if first.left:
            queue.append(first.left)
            
        if first.right:
            queue.append(first.right)
            
    return result
