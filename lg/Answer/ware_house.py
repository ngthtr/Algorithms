
import sys

def getInput():
    global N, arr
    first = input().split()
    N = int (first[0])
    arr = [[0 for i in range(N)] for j in range(N)]
    counter = int (first[1])
    for i in range(counter):
        second = input().split()
        facA = int (second[0]) - 1
        facB = int (second[1]) - 1
        distance = int (second[2])
        arr[facA][facB] = distance
        arr[facB][facA] = distance

getInput()

# N = 5
# arr = [[0, 5, 10, 0, 0], [5, 0, 14, 5, 0], [10, 14, 0, 15, 8], [0, 5, 15, 0, 15], [0, 0, 8, 15, 0]]

class Node:
    current = 0
    distance = 0

    def __init__(self, current, distance):
        self.current = current
        self.distance = distance

    def toString(self):
        return "current = %s, distance = %s" % (self.current, self.distance)


def findMinDistances(node, mask):
    global arr
    queue = [node]
    maxDistance = 0
    while len(queue) > 0:

        dictQueue = {}
        for nodeFake in queue:
            if nodeFake.current in dictQueue.keys():
                if nodeFake.distance < dictQueue[nodeFake.current].distance:
                    dictQueue[nodeFake.current] = nodeFake
            else:
                dictQueue[nodeFake.current] = nodeFake
        queue = list(dictQueue.values())

        queue.sort(key=lambda nodeItem:nodeItem.distance, reverse=True)
        nextNode = queue.pop()
        if mask[nextNode.current-1] == True:
            continue
        mask[nextNode.current-1] = True
        if nextNode.distance > maxDistance:
            maxDistance = nextNode.distance
        # print("=== next node: %s " % nextNode.toString())

        addNodes = []
        for fac in range(1, N+1, 1):
            if mask[fac-1] == False and arr[nextNode.current-1][fac-1] != 0:
                newNode = Node(fac, nextNode.distance + arr[nextNode.current-1][fac-1])
                addNodes.append(newNode)   
        queue += addNodes
    return maxDistance

def main():
    minDistances = sys.maxsize
    for fac in range(1, N+1, 1):
        mask = [False for i in range(N)]
        maxDistance = findMinDistances(Node(fac, 0), mask)
        if maxDistance < minDistances:
            minDistances = maxDistance

    print(minDistances)

main()


