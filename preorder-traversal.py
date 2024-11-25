class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def traverse(root, result, visited):
    if visited.get(root) == None:
        result.append(root.val)
        visited[root] = 1

    if root.left:
        traverse(root.left, result, visited)
    
    if root.right:
        traverse(root.right, result, visited)

    return result
    

def solution(root):
    result = []
    visited = {}
    output = traverse(root, result, visited)

    print(output)


nine = TreeNode(val=9)

eight = TreeNode(val=8, left=nine)

seven = TreeNode(val=7)

six = TreeNode(val=6)

five = TreeNode(val=5, left=six, right=seven)

four = TreeNode(val=4)

three = TreeNode(val=3, right=eight)

two = TreeNode(val=2, left=four, right=five)

root = TreeNode(val=1, left=two, right=three)

solution(root)