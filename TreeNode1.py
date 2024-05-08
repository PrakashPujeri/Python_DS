class TreeNode1:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val,end=" ")
        inorderTraversal(root.right)
root=TreeNode1(5)
root.left=TreeNode1(3)
root.right=TreeNode1(7)
root.left.left=TreeNode1(2)
root.left.right=TreeNode1(4)
root.right.left=TreeNode1(6)
root.right.right=TreeNode1(8)
print("inorder_traversal:",end=" ")
inorderTraversal(root)