# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        par = {}
        
        def findParents(root,parent,par):
            if not root:
                return
            
            par[root] = parent
            findParents(root.left,root,par)
            findParents(root.right,root,par)
        
        def BFS(target,k):
            queue = deque([])
            queue.append(target)
            queue.append("end")
            visited = {}
            while len(queue):
                top = queue[0]
                queue.popleft()
                if(top == "end"):
                    k-=1
                    if(k==0):
                        return queue
                    queue.append("end")
                
                else:
                    visited[top] = 1
                    if(top.left and not top.left in visited):
                        queue.append(top.left)
                    if(top.right and not top.right in visited):
                        queue.append(top.right)
                    if(par[top] and not par[top] in visited):
                        queue.append(par[top])

                    
        if(K==0):
            return [target.val]
        findParents(root,None,par)
        elems = BFS(target,K)
        return [x.val for x in elems]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        