// https://leetcode.com/problems/unique-paths-ii/
class Solution 
{
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        std::vector<std::vector<int>> mask(obstacleGrid.size(), std::vector<int>(obstacleGrid[0].size(), 0));
        mask[0][0] = 1;
        if (obstacleGrid[0][0] == 1)
        {
            return 0;
        }
        for (size_t x = 0; x < n; x++)
        {
            for (size_t y = 0; y < m; y++)
            {
                if (x == 0 && y == 0)
                {
                    continue;
                }
                if (obstacleGrid[x][y] == 1)
                {
                    continue;
                }
                int xtop = x - 1;
                int yleft = y - 1;

                int top = xtop < 0 ? 0 : mask[xtop][y];
                int left = yleft < 0 ? 0 : mask[x][yleft];
                
                mask[x][y] = top + left;
            }
        }

        return mask[n-1][m-1];
    }
};

// https://leetcode.com/problems/unique-paths-ii/
// class Solution 
// {
// public:
//     int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
//         if (obstacleGrid[0][0] == 1)
//         {
//             return 0;
//         }
//         int n = obstacleGrid.size();
//         int m = obstacleGrid[0].size();
//         std::vector<std::vector<bool>> marked(n, std::vector<bool>(m, false));
//         std::vector<std::vector<int>> mask(n, std::vector<int>(m, 0));
//         queue<pair<int, int>> queue;
//         queue.push(pair<int, int>(0, 0));
//         mask[0][0] = 1;
//         while (!queue.empty())
//         {
//             auto node = queue.front();
//             queue.pop();
//             int x = node.first;
//             int y = node.second;
//             marked[x][y] = true;
            
//             if (x + 1 < n && obstacleGrid[x+1][y] == 0)
//             {
//                 mask[x+1][y] += mask[x][y];
//                 if (marked[x+1][y] == false)
//                 {
//                     queue.push(make_pair<int, int>(move(x) + 1, move(y)));
//                     marked[x+1][y] = true;
//                 }
//             }
            
//             if (y + 1 < m && obstacleGrid[x][y+1] == 0)
//             {
//                 mask[x][y+1] += mask[x][y];
//                 if (marked[x][y+1] == false)
//                 {
//                     queue.push(make_pair<int, int>(move(x), move(y) + 1));
//                     marked[x][y+1] = true;
//                 }
//             }
//         }
        
//         return mask[n-1][m-1];
//     }
// };