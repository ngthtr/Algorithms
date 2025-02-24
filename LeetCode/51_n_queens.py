# https://leetcode.com/problems/n-queens/description/
class Solution:
    neigborsX = [0, -1, -1, -1, 0, 1, 1, 1]
    neigborsY = [-1, -1, 0, 1, 1, 1, 0, -1]
    results = []
    n = 0

    def paint(self, x, y, mask):
        mask[x][y] = True
        maskCop = deepcopy(mask)
        for i in range(8):
            nx = x + self.neigborsX[i]
            ny = y + self.neigborsY[i]
            while nx >= 0 and nx < self.n and ny >= 0 and ny < self.n:
                maskCop[nx][ny] = True
                nx += self.neigborsX[i]
                ny += self.neigborsY[i]
        return maskCop

    def createResult(self, path):
        result = [["." for _ in range(self.n)] for _ in range(self.n)]
        for node in path:
            result[node[0]][node[1]] = "Q"
        
        for i in range(self.n):
            result[i] = "".join(result[i])
        self.results.append(result)

    def main(self, row, mask, path):
        if len(path) == self.n:
            self.createResult(path)
            return
        
        for col in range(self.n):
            if mask[row][col] is False:
                pathCop = deepcopy(path)
                pathCop.append([row, col])
                maskCop = self.paint(row, col, mask)
                self.main(row+1, maskCop, pathCop)
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.n = n
        mask = [[False for _ in range(n)] for _ in range(n)]
        self.main(0, mask, [])
        return self.results