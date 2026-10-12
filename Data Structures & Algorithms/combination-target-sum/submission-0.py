class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if (total == target):
                res.append(cur.copy())
                return

            if i >= len(nums) or (total > target):
                return

            # two decisions
            #1. include the number at i 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            #2. do not include the number at i hereafter so increment the pointer if
            cur.pop() #remove the nums[i] added during the first decisions
            dfs(i+1,cur,total)

        dfs(0,[],0) # initial call
        return res
            