class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        unique = set(nums)
        for i in nums:
            length = 1
            if i-1 not in nums:
                j = i
                while j+1 in unique:
                    length += 1
                    j += 1
            if max_length < length:
                max_length = length
        return max_length