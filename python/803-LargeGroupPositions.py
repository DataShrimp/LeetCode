class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) <= 0:
            return []

        ret = []
        start = end = 0
        while end != len(S):
            if S[start]!=S[end]:
                if (end-start) >= 3:
                    ret.append([start, end-1])
                start = end
            end = end + 1
        if (end - start) >= 3:
            ret.append([start, end-1])
        return ret


if __name__ == "__main__":
    S = "abcdddeeeeaabbbcd"
    print(Solution().largeGroupPositions(S))