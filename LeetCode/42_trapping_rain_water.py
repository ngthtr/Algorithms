class Solution {
public:
    int trap(vector<int>& height) {

        int startId = 0;
        for (int i = 1; i < height.size(); i++)
        {
            if (height[i] >= height[startId])
            {
                startId = i;
            } else {
                break;
            }
        }
        // cout << "startId = " << startId << endl;

        int result = 0;
        vector<int> increaseVec;
        for (int i = startId; i < height.size(); i++)
        {
            // cout << "i = " << i << endl;
            if (i == startId)
            {
                increaseVec.push_back(height[i]);
                continue;
            }

            if (height[i] <= increaseVec.back())
            {
                increaseVec.push_back(height[i]);
            }
            else {
                if (height[i] >= increaseVec[0])
                {
                    while (increaseVec.size() > 0)
                    {
                        result += increaseVec[0] - increaseVec.back();
                        increaseVec.pop_back();
                    }
                } 
                else
                {
                    int j = increaseVec.size()-1;
                    while (increaseVec[j] < height[i])
                    {
                        result += height[i] - increaseVec[j];
                        increaseVec[j] = height[i];
                        j--;
                    }
                }
                increaseVec.push_back(height[i]);
            }

        }
        return result;
    }
};