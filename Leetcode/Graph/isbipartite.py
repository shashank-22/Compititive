from collections import defaultdict
class Solution:
      
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def makegraph(dislikes,graph):
            for i in dislikes:
                graph[i[0]-1].append(i[1]-1)
                graph[i[1]-1].append(i[0]-1)
        def dfs(graph,u ,colorswitch):
            if colorswitch:
                dfs.color[u] = 'B'
            else:
                dfs.color[u] = 'R'

            for j in range(len(graph[u])):
                if(colorswitch and dfs.color[graph[u][j]] == "B") or (not colorswitch and dfs.color[graph[u][j]] == "R"):
                    dfs.isbipartite  = 0
                    return
                elif(dfs.color[graph[u][j]] == 'U'):
                    if(dfs.isbipartite):
                        dfs(graph,graph[u][j],(colorswitch+1)%2)
                    else:
                        return
                    
        
        graph = defaultdict(list)
        makegraph(dislikes,graph)
        dfs.color = ['U']*N
        dfs.isbipartite = 1
        for i in range(N):
            if(dfs.color[i] == 'U'):
                dfs(graph,i,0)
        
        return dfs.isbipartite 