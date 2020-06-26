# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
class Solution:
    def trav(self,root,num,sum=0):
        if(not root):
            return None
        if(root.left==None and root.right==None):
            num[0]+=sum*10+root.val
            
        if(root.left):
            self.trav(root.left,num,sum*10+root.val)
        if(root.right):
            self.trav(root.right,num,sum*10+root.val)
        
        
    def sumNumbers(self, root: TreeNode) -> int:
        num=[0]
        self.trav(root,num,sum=0)
        return num[0]