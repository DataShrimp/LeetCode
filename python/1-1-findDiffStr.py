class Solution:
    def findDiffStr(self, s):
        m = {}
        ret = 1
        for w in s:
            if w in m.keys():
                ret = 0
                break
            m[w] = 1
        return ret

if __name__ == "__main__":
    s = "abcd"
    print(Solution().findDiffStr(s))