# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        
        def traverse(root,lst,cursum):
            if not root:
                return
            cursum+=root.val
            if(cursum==sum):
                traverse.res+=1
            
            traverse.res += lst[cursum-sum]
            lst[cursum]+=1
            traverse(root.left,lst,cursum)
            traverse(root.right,lst,cursum)
            lst[cursum]-=1
            
        traverse.res=0
        lst = defaultdict(int)  
        traverse(root,lst,0)
        return traverse.res
        