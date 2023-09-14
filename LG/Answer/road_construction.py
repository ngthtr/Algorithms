


N = 0
arr = []


# N = 3
# arr = [[0,4,1], [2,5,3], [6,2,0]]

def getInput():
	global arr, N
	N = int (input())
	for n in range(N):
		data = input()
		item = []
		for i in range(N):
			item.append(int (data[i]))
		arr.append(item)


getInput()

class Node:
	def __init__(self, x, y, distance):
		self.x = x
		self.y = y
		self.distance = distance

def minRoad():
	global N
	marked = [[False for i in range(N)] for j in range(N)]
	marked[0][0] = True
	listNode = []
	node = Node(0, 0, 0)
	while node.x != N-1 or node.y != N-1:
		if node.x < N-1 and marked[node.x+1][node.y] == False:
			listNode.append(Node(node.x+1, node.y, node.distance + arr[node.x+1][node.y]))
		if node.x > 0 and marked[node.x-1][node.y] == False:
			listNode.append(Node(node.x-1, node.y, node.distance + arr[node.x-1][node.y]))
		if node.y < N-1 and marked[node.x][node.y+1] == False:
			listNode.append(Node(node.x, node.y+1, node.distance + arr[node.x][node.y+1]))
		if node.y > 0 and marked[node.x][node.y-1] == False:
			listNode.append(Node(node.x, node.y-1, node.distance + arr[node.x][node.y-1]))
			
		listNode.sort(key=lambda node: node.distance, reverse=True)
		node = listNode.pop()
		marked[node.x][node.y] = True

	print(node.distance)
minRoad()