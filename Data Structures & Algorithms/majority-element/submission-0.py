from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = Counter(nums)
        max = 0
        max_i = 0
        for i in map:
            if map[i] > max:
                max = map[i]
                max_i = i
        if max > len(nums)/2:
            return max_i