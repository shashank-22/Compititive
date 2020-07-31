# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if(not root):
                return
            
            inorder(root.left)
            if(not inorder.ele1):
                if(root.val<inorder.prev.val):
                    inorder.ele1 = inorder.prev
                    inorder.ele2 = root
            elif(root.val<inorder.ele1.val):
                inorder.ele2 = root
            inorder.prev = root   
            inorder(root.right)
        
        inorder.ele1 = None
        inorder.ele2 = None
        inorder.prev = TreeNode(-99999999999999)
        inorder(root)
        inorder.ele1.val, inorder.ele2.val = inorder.ele2.val, inorder.ele1.val
        