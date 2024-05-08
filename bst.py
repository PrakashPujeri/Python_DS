class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        # Traverse left subtree
        inorder_traversal(node.left)
        # Visit root node
        print(node.value, end=' ')
        # Traverse right subtree
        inorder_traversal(node.right)

# Example usage:
# Creating a BST with nodes 5, 3, 10
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(10)

# Perform inorder traversal
print("Inorder traversal:")
inorder_traversal(root)  
