// Leetcode 874 (TODO)

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int x = 0;
        int y = 0;
        int direction = 0; // 0,1,2,3 for N,E,S,W
        for (vector<int>::iterator iter = commands.begin(); iter != commands.end(); iter++) {
            if (*iter == -2) {
                direction = (direction + 4 - 1) % 4;
                continue;
            }
            if (*iter == -1) {
                direction = (direction + 1) % 4;
                continue;
            }
            if (*iter >= 1 && *iter <= 9) {
                int step = *iter;
                switch (direction) {
                    case 0:
                        for (int i = 0; i < obstacles.size(); i++) {
                            if (obstacles[i][0] == x && obstacles[i][1] > y && obstacles[i][1] <= y + step) {
                                step = obstacles[i][1] - 1;
                                step = (step > y) ? step-y : 0;
                            }
                        }
                        y = y + step;
                        break;
                    case 1:
                        for (int i = 0; i < obstacles.size(); i++) {
                            if (obstacles[i][1] == y && obstacles[i][0] > x && obstacles[i][0] <= x + step) {
                                step = obstacles[i][0] - 1;
                                step = (step > x) ? step-x : 0;
                            }
                        }
                        x = x + step;
                        break;
                    case 2:
                        for (int i = 0; i < obstacles.size(); i++) {
                            if (obstacles[i][0] == x && obstacles[i][1] < y && obstacles[i][1] >= y - step) {
                                step = obstacles[i][1] + 1;
                                step = (step < y)? y-step: 0;
                            }
                        }
                        y = y - step;
                        break;
                    case 3:
                        for (int i = 0; i < obstacles.size(); i++) {
                            if (obstacles[i][1] == y && obstacles[i][0] < x && obstacles[i][0] >= x - step) {
                                step = obstacles[i][0] + 1;
                                step = (step < x)? x-step: step;
                            }
                        }
                        x = x - step;
                        break;
                    }
            }
        }
        return x * x + y * y;
    }
};

int main() {
    int arr1[5] = {7,-2,-2,7,5};
    int arr2[10][2] = {{-3,2},{-2,1},{0,1},{-2,4},{-1,0},{-2,-3},{0,-3},{4,4},{-3,3},{2,2}};

    vector<int> cmd;
    for (int i=0; i<sizeof(arr1)/sizeof(arr1[0]); i++) {
        cmd.push_back(arr1[i]);
        std::cout << arr1[i] << " ";
    }

    vector<vector<int>> obs;
    for (int i=0; i<sizeof(arr2)/sizeof(arr2[0]); i++) {
        vector<int> ob;
        ob.push_back(arr2[i][0]);
        ob.push_back(arr2[i][1]);
        obs.push_back(ob);
        std::cout << arr2[i][0] << ", " << arr2[i][1] << std::endl;
    }

    Solution s;
    cout << s.robotSim(cmd, obs);
}