class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        num = R * C
        i = 0
        l = 2
        idx = 0
        j = 0    # 规律：方向改变2次，长度加1，按长度遍历
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        ret = []
        while num > len(ret):
            # filter
            if r0>=0 and r0<R and c0>=0 and c0<C:
                ret.append([r0,c0])

            if i<2:
                r0 += dir[idx%4][0]
                c0 += dir[idx%4][1]
                i += 1
                if i <= 1:
                    idx += 1
                continue

            # case i>2
            if j < l*2:
                if j%l == 0:
                    idx += 1
                j += 1

            r0 += dir[idx%4][0]
            c0 += dir[idx%4][1]

            if j == l*2:
                l += 1
                j = 0

        return ret

if __name__ == "__main__":
    print(Solution().spiralMatrixIII(5, 6, 1, 4))