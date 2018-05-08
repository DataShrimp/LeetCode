class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            i = i+1
        return nums

if __name__ == "__main__":
    nums = [1,1,2,2,3]
    print(Solution().removeDuplicates(nums))