from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        n = len(nums)+1
        bucket = [[] for _ in range(n)]
        for i in map:
            bucket[map[i]].append(i)

        count = 0
        res = []
        for i in range(len(bucket)-1,-1,-1):
            if len(bucket[i]) != 0:
                for j in bucket[i]:
                    res.append(j)
                    count += 1  
            if count == k:
                break
        return res

