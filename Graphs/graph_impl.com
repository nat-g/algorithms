class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	def getConnections(self):
		return self.connectedTo.keys()

	def __str__(self):		# String representation of an object
		return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

class Graph:
	def __init__(self):
		self.vertList = {} # Dictionary (key):(Vertex object)
		self.vertNum = 0

	def addVertex(self,key):
		self.vertNum += 1
		a = Vertex(key)
		self.vertList[key] = a
		return a

	def getVertex(self,v):
		if v in self.vertList:
			return self.vertList[v]
		else:
			return None

	def addEdge(self,v1,v2,cost=0):
		if v1 not in self.vertList:
			addVertex(v1)
		elif v2 not in self.vertList:
			addVertex(v2)
		self.vertList[v1].addNeighbor(self.vertList[v2],cost)

	def __contains__(self,v):
		return self.vertList[v]

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

g = Graph()
for i in range(6):
	g.addVertex(i)
	g.vertList


g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

print g.getVertex(1)
print g.getVertices()
print g.__contains__(3)
print g.__iter__()
