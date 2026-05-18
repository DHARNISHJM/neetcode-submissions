class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0,len(nums)):
            x = target - nums[i]
            if x in map:
                return [min(i,map[x]),max(i,map[x])]
            else:
                map[nums[i]] = i
        