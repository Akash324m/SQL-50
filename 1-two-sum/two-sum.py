class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x==y:
                    continue
                elif nums[x]+nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result
        