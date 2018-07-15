#include <iostream>
#include <vector>

// WC93, id: 868

using namespace std;

class Solution {
public:
    int binaryGap(int N) {
        vector<int> binList;
        while (N != 0) {
            int bin = N % 2;
            binList.push_back(bin);
            N = N / 2;
        }

        int start = -1;
        int end = -1;
        int maxLength = 0;
        for(vector<int>::iterator it=binList.begin(); it!=binList.end(); it++) {
            // cout << *it << ",";
            if (*it ==  1) {
                if (end == start) {
                    end = it - binList.begin();
                }
                else {
                    start = end;
                    end = it - binList.begin();
                    if (end - start > maxLength) {
                        maxLength = end - start;
                    }
                }
            }
        }
        return maxLength;
    }
};


int main1() {
    Solution solution;
    cout << solution.binaryGap(22) << endl;
    return 0;
}
