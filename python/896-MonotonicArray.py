class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        diff1 = []
        for i in range(1,len(A)):
            diff1.append(A[i] - A[i-1])

        if max(diff1) >= 0 and min(diff1) >=0:
            return True
        if max(diff1) <=0 and min(diff1) <= 0:
            return True
        return False

if __name__ == "__main__":
    print(Solution().isMonotonic([1,3,2,5]))
