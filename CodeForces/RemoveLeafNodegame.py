# class Node:
# 	def __init__(self,key):
# 		self.data = key
# 		self.edges = []
class Graph:
	def __init__(self,vertices):
		self.vertices = [[] for i in range(vertices)]
	def addedge(self,node1,node2):
		self.vertices[node1].append(node2)
		self.vertices[node2].append(node1)
	def removeedge(self,node1,node2):
		self.vertices[node1].remove(node2)
		self.vertices[node2].remove(node1)

t = int(input().strip())

while t:
	n,target = map(int,input().strip().split(" ")) 
	gph = Graph(n)
	for i in range (n-1):
		node1,node2 = map(int,input().strip().split(" ")) 
		gph.addedge(node1-1,node2-1)
	
	if(n==1 or len(gph.vertices[target-1])==1):
	    print('Ayush')
	    t-=1
	    continue
	target-=1
	flag=1
	turn=0
	while(flag):
		flag=0
		for i in range(0,n):
			if(i==target):
				continue
			elif(len(gph.vertices[i])==1):
				if(gph.vertices[i][0]!=target):
					gph.removeedge(i,gph.vertices[i][0])
					flag=1
					turn=(turn+1)%2
	
	if((turn+len(gph.vertices[target]))%2):
		print("Ayush")
	else:
		print("Ashish")
	t-=1