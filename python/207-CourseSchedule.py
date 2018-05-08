# 检查图的连通性，看是否有循环连接

import numpy as np

class Solution:
    # ok but will timeout
    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        m = np.zeros((numCourses, numCourses))
        r = m
        for edge in prerequisites:
            m[edge[0],edge[1]] = 1
        k = m
        for i in range(numCourses):
            print(r)
            m = m.dot(k)
            r = r + m

        ret = True
        for i in range(numCourses):
            if r[i,i] >= 1:
                ret = False
                break
        return ret

    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        # init
        for x,y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i]==-1:
                return False
            if visit[i]==1:
                return True
            visit[i]=-1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i]=1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

if __name__ == "__main__":
    print(Solution().canFinish(3, [[1,0],[0,2],[2,1]]))
    #print(Solution().canFinish(3, [[0, 2], [1, 2], [2, 0]]))
    Solution().canFinish(500,[[481,475],[196,63],[438,33],[212,328],[268,20],[226,288],[436,487],[199,494],[421,279],[369,14],[92,91],[183,174],[271,15],[4,435],[435,47],[217,460],[216,319],[468,125],[115,1],[435,383],[192,136],[86,103],[336,342],[5,301],[255,253],[185,37],[323,168],[417,241],[151,208],[347,53],[180,329],[198,452],[31,419]])
