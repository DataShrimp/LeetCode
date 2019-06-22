# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def increasingBST(self, root):
        array = []
        self.BST(root, array)
        array.sort()
        r = TreeNode(array[0])
        p = r
        for i in range(1, len(array)):
            p.left = None
            p.right = TreeNode(array[i])
            p = p.right
        return r

    def BST(self, root, array):
        if root != None:
            array.append(root.val)
            if root.left != None:
                self.BST(root.left, array)
            if root.right != None:
                self.BST(root.right, array)

    def increasingBST2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        array = [x for x in root if x is not None]
        array.sort()
        out = []
        for x in array:
            out.append(x)
            out.append(None)
        out.pop()
        return out

if __name__ == "__main__":
    root = TreeNode(379)
    root.left = TreeNode(826)
    root.left.left = None
    root.left.right = None
    root.right = None
    Solution().increasingBST(root)
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = None
    root.left.right = TreeNode(4)
    root.left.right.left = None
    root.left.right.right = None
    root.right.left = None
    root.right.right = None
    Solution().increasingBST(root)
    """

    #print(Solution().increasingBST([5,3,6,2,4,None,8,1,None,None,None,7,9]))
