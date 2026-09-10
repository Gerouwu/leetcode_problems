class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hit = 0
        for n in range(len(nums)):
            sum = 0
            for i in nums[n:]:
                sum += i
                if sum == k:
                    hit+=1
        return hit
test = Solution()
print(test.subarraySum([1,2,3],3))