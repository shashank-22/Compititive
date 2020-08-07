# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# same level values should be sorted
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def BFS(target):
            queue = deque([])
            k=0
            queue.append((target,k))
            queue.append(("end",0))
            tempmap = defaultdict(list)
            while len(queue):
                top,level = queue[0]
                queue.popleft()
                if(top=="end"):
                    queue.append(("end",0))
                    if(queue[0]==("end",0)):
                        return
                    
                    for x in tempmap.keys():
                        BFS.map[x].extend(sorted(tempmap[x]))
                    tempmap = defaultdict(list)
                else:
                    tempmap[level].append(top.val)
                    if(top.left):
                        queue.append((top.left,level-1))
                    if(top.right ):
                        queue.append((top.right,level+1))
                
        BFS.map = defaultdict(list)
        BFS(root)
        return [BFS.map[x] for x in sorted(BFS.map.keys())]
        