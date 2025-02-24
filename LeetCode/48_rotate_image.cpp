// https://leetcode.com/problems/rotate-image/description/

class Solution {
    public:
        void switchDirection(int &directX, int &directY)
        {
            if (directX == 0 && directY == 1)
            {
                directX = 1;
                directY = 0;
                return;
            }
            if (directX == 1 && directY == 0)
            {
                directX = 0;
                directY = -1;
                return;
            }
            if (directX == 0 && directY == -1)
            {
                directX = -1;
                directY = 0;
                return;
            }
            if (directX == -1 && directY == 0)
            {
                directX = 0;
                directY = 1;
                return;
            }
        }
    
        void rotate(vector<vector<int>>& matrix) {
            int length = matrix.size();
            vector<vector<int>> result(length, vector<int>(length, 0));
            if (length % 2 == 1)
            {
                result[length/2][length/2] = matrix[length/2][length/2];
            }
    
            for (int i = 0; i < length/2; i++)
            {
                int directX1 = 0;
                int directY1 = 1;
                int curX1 = i;
                int curY1 = i;
    
                int directX2 = 1;
                int directY2 = 0;
                int curX2 = i;
                int curY2 = length - i - 1;
                
                while (true)
                {
                    result[curX2][curY2] = matrix[curX1][curY1];
    
                    int x = curX1 + directX1;
                    int y = curY1 + directY1;
                    if (x >= length - i || x < i || y >= length - i || y < i)
                    {
                        switchDirection(directX1, directY1);
                        switchDirection(directX2, directY2);
                    }
                    curX1 += directX1;
                    curY1 += directY1;
                    curX2 += directX2;
                    curY2 += directY2;
                    if (curX1 == i && curY1 == i)
                    {
                        break;
                    }
                }
            }
            matrix = result;
        }
    };