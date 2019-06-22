// Leetcode 872

#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> leaves1;
    vector<int> leaves2;

    bool leafSimilar(TreeNode *root1, TreeNode *root2) {
        dfs(root1, leaves1);
        dfs(root2, leaves2);
        if (leaves1.size() == leaves2.size()) {
            for (int i=0; i<leaves1.size(); i++) {
                if (leaves1[i] == leaves2[i])
                    continue;
                else
                    return false;
            }
            return true;
        } else {
            return false;
        }
    }

    void dfs(TreeNode *root, vector<int> &leaves) {
        if (root == NULL)
            return;

        // visit root
        if (root->left == NULL && root->right == NULL){
            leaves.push_back(root->val);
            cout << root->val << endl;
        }
        else {
            if (root->left != NULL)
                dfs(root->left, leaves);
            if (root->right != NULL)
                dfs(root->right, leaves);
        }
    }
};

int main5() {
    Solution s;
    TreeNode root(3);
    root.left = new TreeNode(5);
    root.right = new TreeNode(1);
    root.left->left = new TreeNode(4);
}
