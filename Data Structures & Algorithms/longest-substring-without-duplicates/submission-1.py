class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        max_length = 0
        for right in range(left, len(s)):
            # if s[right] not in unique:
            #     unique.add(s[right])
            # else:
            #     while s[right] in unique:
            #         unique.remove(s[left])
            #         left += 1
            #     unique.add(s[right])
            if s[right] in unique:
                while s[right] in unique:
                    unique.remove(s[left])
                    left += 1
            unique.add(s[right])
            length = right - left + 1
            if max_length < length:
                max_length = length
        return max_length