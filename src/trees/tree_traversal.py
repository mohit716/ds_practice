class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Build this tree:
#       1
#      / \
#     2   3
#    / \
#   4   5


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder Traversal function (outside the class)
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value, end=' ')
    inorder_traversal(node.right)

# Call it
print("Inorder traversal:")
inorder_traversal(root)