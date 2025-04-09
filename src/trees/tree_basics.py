class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Test output
print("Root:", root.value)
print("Left Child:", root.left.value)
print("Right Child:", root.right.value)