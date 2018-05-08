class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    def findMode(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        if not root:
            return []
        count = collections.Counter()
        self.dfs(root, count)
        max_ct = max(self.count.values())
        return [k for k,v in self.count.items() if v==max_ct]


    def dfs(self, node, count):
        if node != None:
            count[node.val] += 1
            self.dfs(node.left, count)
            self.dfs(node.right, count)

if __name__ == "__main__":
    #root = TreeNode(1)
    #root.right = TreeNode(2)
    #root.right.left = TreeNode(2)
    root = TreeNode(2147483647)

    print(Solution().findMode(root))