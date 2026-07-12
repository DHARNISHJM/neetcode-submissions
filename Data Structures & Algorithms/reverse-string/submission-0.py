class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        temp = ""
        for i in range(0,len(s)//2):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left = left + 1
            right = right - 1