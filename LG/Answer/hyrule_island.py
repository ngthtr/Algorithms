from copy import copy, deepcopy

NOT = "#"
EMPTY = "."
R = 0
C = 0
N = 0
S = 0
F = 0
arrData = []
mask = None
shrines = []

class Shrine:
    x = 0
    y = 0
    number = None
    distance = 0
    def __init__(self, x, y, number, distance):
        self.x = x
        self.y = y
        self.number = number
        self.distance = distance

    def toString(self):
        return "x = %s, y = %s, number = %s, distance = %s" % (self.x, self.y, self.number, self.distance)

def getInput():
    global R, C, N, S, F, arrData, mask, shrines
    arrInput = input().split(" ")
    R = int (arrInput[0])
    C = int (arrInput[1])
    N = int (arrInput[2])
    S = int (arrInput[3])
    F = int (arrInput[4])

    mask = [[False for c in range(C)] for r in range(R)]

    for r in range(R):
        arrItem = list(input())
        arrData.append(arrItem)
        for c in range(C):
            if arrItem[c] == NOT:
                mask[r][c] = True
            if arrItem[c] not in [NOT, EMPTY]:
                shrines.append(Shrine(r, c, int(arrData[r][c]), 0))

def explore8(shrine, finishShrine, mask):
    maxR = len(mask) - 1
    maxC = len(mask[0]) - 1 
    arrX = [-1, -1, -1, 0, 1, 1, 1, 0]
    arrY = [-1, 0, 1, 1, 1, 0, -1, -1]

    additionalShrines = []
    for i in range(len(arrX)):
        nX = shrine.x + arrX[i]
        nY = shrine.y + arrY[i]

        if nX >= 0 and nX <= maxR and nY >= 0 and nY <= maxC and mask[nX][nY] == False:
            mask[nX][nY] = True
            if arrData[nX][nY] == str(finishShrine.number):
                return None, shrine.distance+1
            additionalShrines.append(Shrine(nX, nY, None, shrine.distance+1))
    return additionalShrines, None


def calculateDistanceShrines(startShrine, finishShrine, mask):
    # print("calculateDistanceShrines: start = %s, finish = %s" % (startShrine.number, finishShrine.number))
    queue = [startShrine]
    while len(queue) > 0:
        queue.sort(key=lambda shrineItem:shrineItem.distance, reverse=True)
        shrine = queue.pop()
        additionalShrines, distance = explore8(shrine, finishShrine, mask)
        if additionalShrines != None:
            queue += additionalShrines
        if distance != None:
            return distance
    return None

def createMapDistanceShrines():
    mapShrines = [[0 for r in range(N)] for c in range(N)]
    global shrines
    shrines.sort(key=lambda shrine:shrine.number)
    for startShrine in range(N-1):
        for finishShrine in range(startShrine+1, N):
            maskCopy = deepcopy(mask)
            distance = calculateDistanceShrines(shrines[startShrine], shrines[finishShrine], maskCopy)
            if distance == None:
                return None
            mapShrines[startShrine][finishShrine] = distance
            mapShrines[finishShrine][startShrine] = distance
    return mapShrines


def findMinPath(mapShrines):
    global shrines

    mask = [False for i in range(N)]
    mask[S-1] = True

    availableShrines = [i for i in range(N)]
    availableShrines.remove(F-1)
    foundShrines = 0

    shrines.sort(key=lambda shrineItem:shrineItem.number)
    queue = [Shrine(S-1, S-1, S-1, 0)]
    while len(queue) > 0:
        queue.sort(key=lambda shrineItem:shrineItem.distance, reverse=True)
        shrine = queue.pop()
        for shrineItem in queue:
            queue.remove(shrineItem)
        if shrine.number == F-1:
            print(shrine.distance)
            return
        mask[shrine.number] = True

        # print("shrine: %s" % shrine.toString())

        foundShrines += 1
        if foundShrines == N-1:
            availableShrines.append(F-1)

        additionalShrines = []
        for i in range(N):
            if mask[i] == False and i in availableShrines and mapShrines[shrine.number][i] != 0:
                additionalShrine = Shrine(i, shrine.number, i, shrine.distance + int(mapShrines[shrine.number][i]))
                additionalShrines.append(additionalShrine)
        queue += additionalShrines


getInput()
mapShrines = createMapDistanceShrines()
if mapShrines == None:
    print(-1)
else:
    # for item in mapShrines:
    #     print(item)

    findMinPath(mapShrines)