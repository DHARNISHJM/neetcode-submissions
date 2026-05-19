class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansMap = {}
        for i in strs:
            counter = [0 for i in range(0,26)]
            for j in i:
                counter[ord(j)-97] += 1
            t_counter = tuple(counter)
            if t_counter not in ansMap:
                ansMap[t_counter] = [i]
            else:
                ansMap[t_counter].append(i)
        return list(ansMap.values())
