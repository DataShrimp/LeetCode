import math
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        len = 2
        ret = 0
        l = list(range(1,N))
        # time limited
        while N > len:
            temp = N/len
            a = int(math.floor(temp) - math.ceil(len/2))
            sub = l[a : (a+len)]
            if sum(sub) == N:
                print(sub)
                ret = ret + 1
            if a<0:
                break
            len = len + 1
        return ret+1



if __name__ == "__main__":
    N = 3
    print(Solution().consecutiveNumbersSum(N))