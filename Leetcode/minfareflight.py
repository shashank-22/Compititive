class Solution:
    class flightcost:
        def __init__(self,lst,cost):
            self.path = lst
            self.cost = cost

    def notvisited(self,path,z):
        for i in path:
            if(i==z):
                return 0
        return 1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        sadjmat = [[-1 for i in range(n)] for i in range(n)]
        for i in flights:
            s,d,p = i[0],i[1],i[2]
            sadjmat[s][d] = p
        
        minfare = 99999999999999
        temppath = self.flightcost([src],0)
        q = []
        q.append(temppath)
        while(len(q)):
            temppath = q.pop(0)
            if(temppath.path[-1]==dst):
                if(minfare>temppath.cost):
                    minfare = temppath.cost
            else:
                if(len(temppath.path)-1<=K):
                    for z in range(0,n):
                        if(sadjmat[temppath.path[-1]][z]!=-1 and self.notvisited(temppath.path,z) and temppath.cost+sadjmat[temppath.path[-1]][z]<minfare):
                            templist = []
                            templist+=temppath.path
                            templist.append(z)
                            q.append(self.flightcost(templist,temppath.cost+sadjmat[temppath.path[-1]][z]))
        if(minfare!=99999999999999):
            return minfare
        return -1