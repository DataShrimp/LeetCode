class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words = A.split(" ") + B.split(" ")
        ret = []
        for word in words:
            if words.count(word) == 1:
                ret.append(word)
        return ret

if __name__ == "__main__":
    A = "this apple is sweet"
    B = "this apple is sour"
    C = Solution().uncommonFromSentences(A, B)
    print(C)
