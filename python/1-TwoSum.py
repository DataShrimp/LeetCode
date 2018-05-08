class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

    # failed [3,3], target=6
    def twoSum3(self, nums, target):
        d = dict(zip(nums, range(len(nums))))
        ret = []
        for k in d.keys():
            r = target - k
            if r in d:
                ret = [d[k], d[r]]
                break
        return ret

    # 时间复杂度高
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ret = [i,j]
                    break
            if len(ret)==2:
                break
        return ret

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    print(Solution().twoSum(nums, target))