

arr = []
N = 0
def getInput():
    global N, arr
    N = int (input())
    for i in range(N):
        data = input()
        items = []
        for c in data:
            items.append(int (c))
        arr.append(items)

getInput()
# arr = [[1, 2, 3, 0], [1, 7, 3, 7], [1, 7, 7, 7], [0, 2, 2, 0]]

class Node:
    def __init__(self, color, colors):
        self.color = color
        self.colors = colors
    def toString(self):
        return "color: %s, colors: %s" % (self.color, self.colors)

arrNode = [[Node(0, []) for i in range(N)] for i in range(N)]

def getArrColors(arr):
    arrColors = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] not in arrColors and arr[x][y] != 0:
                arrColors.append(arr[x][y])
    return arrColors

def getAreaColor(color):
    minX = -1
    minY = -1
    maxX = 10
    maxY = 10
    for x in range(N):
        for y in range(N):
            if arr[x][y] == color:
                if (x <= minX and y <= minY) or (minX == -1 and minY == -1):
                    minX = x
                    minY = y
                if (x >= maxX and y >= maxY) or (maxX == 10 and maxY == 10):
                    maxX = x
                    maxY = y
    return minX, minY, maxX, maxY

def paintColor(arrColors):
    for color in arrColors:
        minX, minY, maxX, maxY = getAreaColor(color)
        # print("color: %s, minX = %s, minY = %s, maxX = %s, maxY = %s" % (color, minX, minY, maxX, maxY))
        for x in range(N):
            for y in range(N):
                if x >= minX and y >= minY and x <= maxX and y <= maxY:
                    arrNode[x][y].color = arr[x][y]
                    arrNode[x][y].colors.append(color)


arrColors = getArrColors(arr)
paintColor(arrColors)

# for x in range(N):
#     for y in range(N):
#         print(arrNode[x][y].toString())

for x in range(N):
    for y in range(N):
        if len(arrNode[x][y].colors) > 1 and arrNode[x][y].color in arrColors:
            arrColors.remove(arrNode[x][y].color)
print(len(arrColors))