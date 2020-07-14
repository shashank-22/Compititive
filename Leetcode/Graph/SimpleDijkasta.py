
class Graph:
    def __init__(self,v):
        self.adjmat = [[] for i in range (v)]
        
    def iniltilizeGraph(self,vertices):
        for edge in vertices:
            self.adjmat[edge[0]-1].append([edge[1]-1, edge[2]])
    
    def getMinimumDistVertexNotRelaxed(self, dist,visited):
        
        minimum = 7000
        minnode = 0
        
        for i in range(len(visited)):
            if(visited[i]==False and dist[i]<minimum):
                minimum = dist[i]
                minnode = i
        return minnode
            
    def dijkstra(self,source):
        visited = [False]*len(self.adjmat)
        dist = [7000]*len(self.adjmat)
        dist[source] = 0
        
        for _ in range(len(self.adjmat)):
            
            u = self.getMinimumDistVertexNotRelaxed(dist,visited)
            
            visited[u] = True
            
            for v in range(len(self.adjmat[u])):
                if(not visited[self.adjmat[u][v][0]] and dist[self.adjmat[u][v][0]] > dist[u] +self.adjmat[u][v][1] ):
                    dist[self.adjmat[u][v][0]] = dist[u] +self.adjmat[u][v][1]
        
        return dist

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        grp = Graph(N)
        grp.iniltilizeGraph(times)
        
        delay = grp.dijkstra(K-1)
        
        maxdelay = 0
        for i in delay:
            if(i==7000):
                return -1
            else:
                maxdelay = max(i,maxdelay)
        return maxdelay
        