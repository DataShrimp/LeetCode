class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        method = 3
        if method == 1:
            # 1. brute search
            return self.climb1(0, n)
        elif method == 2:
            # 2. burte search with memory
            memo = [0]*n
            return self.climb2(0, n, memo)
        elif method == 3:
            # 3. dynamic programming (Also, Fibonacci Number)
            if n == 1:  # to avoid the out of index bug when n==1
                return 1
            dp = [0]*n
            dp[0] = 1
            dp[1] = 2
            for i in range(2,n):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n-1]

    def climb1(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb1(i+1,n)+self.climb1(i+2,n)

    def climb2(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb2(i + 1, n, memo) + self.climb2(i + 2, n, memo)
        return memo[i]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(10))