# idea: 快慢指针，如果有循环，则快慢指针一定会相遇

class Solution(object):
    # cannot define yet
    def circularArrayLoop2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        temp = 0
        ret = False
        n = len(nums)
        for i in range(n):
            temp = nums[i]
            sum = temp
            if sum%n == 0:
                ret = True
                break
            print(i, sum)
            temp = nums[(i+sum)%n]
            sum += temp
        return ret

    def circularArrayLoop(self, nums):
        n = len(nums)
        for i in range(n):
            j = i
            k = self.getIndex(i, nums)
            print(i, j, k, nums[i], nums[k], nums[self.getIndex(k,nums)])
            # 快慢指针是朝一个方向
            while nums[k]*nums[i]>0 and nums[self.getIndex(k,nums)]*nums[i]>0:
                print(i, j, k)
                if j==k:
                    # 如果形成了闭环（死循环）则退出
                    if j==self.getIndex(j, nums):
                        break
                    return True
                j = self.getIndex(j, nums)
                k = self.getIndex(self.getIndex(k, nums), nums)
        return False

    def getIndex(self, i, nums):
        n = len(nums)
        return (i+nums[i])%n # + (i+nums[i] < 0)*n

if __name__ == "__main__":
    print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))
    print(Solution().circularArrayLoop([-1,2]))
    print(Solution().circularArrayLoop([1,2,3,4,5]))