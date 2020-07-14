class Graph:
    def __init__(self,v):
        self.adjmat = defaultdict(list)
        
    def iniltilizeGraph(self,vertices):
        for edge in vertices:
            self.adjmat[edge[0]].append(edge[1])
            self.adjmat[edge[1]].append(edge[0])
            
    def countLevelsUsingBFS(self, root):
        q = []
        visited = [False]*len(self.adjmat)
        q.append(root)
        visited[root] = True
        level = 0
        q.append("end")
        count = 0
        while(len(q)):
            top = q.pop(0)
            if(top == "end"):
                if(count==0):
                    return level
                level+=1
                q.append("end")
                count = 0 
                
            else:
                for v in range(len(self.adjmat[top])):
                    if(not visited[self.adjmat[top][v]]):
                        visited[self.adjmat[top][v]] = True
                        q.append(self.adjmat[top][v])
                        count+=1
            
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if(n==1):
            return [0]
        gph = Graph(n)
        gph.iniltilizeGraph(edges)
        minlist = []
        mini = 1000000009
        for v in range(n):
            levels = gph.countLevelsUsingBFS(v)
            if(levels<mini):
                minlist = [v]
                mini = levels
            elif(levels==mini):
                minlist.append(v)
        return minlist