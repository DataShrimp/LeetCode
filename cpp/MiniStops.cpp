// Leetcode 871 (TODO)
#include <iostream>
#include <vector>

using namespace std;

class Node {
public:
    int dist = 0;
    int fuel = 0;

    vector<Node> childs;
};

// dfs and branch bounds
int main3() {
    int target = 100;
    int startFuel = 10;
    int stations[4][2] = {{10,60},{20,30},{30,30},{60,40}};

    // states
    Node node;
    node.dist = startFuel;
    node.fuel = startFuel;

    //while (node.dist < target)
    {
        // search child station
        for (int i=0; i<4; i++) {
            if (stations[i][0] < node.fuel) {
                Node tmp;
                tmp.fuel = node.fuel - stations[i][1] + stations[i][0];
                tmp.dist = stations[i][1] + tmp.fuel;
                node.childs.push_back(tmp);
            }
        }
    }

    cout << "hello" << endl;
    return 1;
}