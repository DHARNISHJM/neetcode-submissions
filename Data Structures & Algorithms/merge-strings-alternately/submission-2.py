class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        res = []
        while len(word1) > p1 and len(word2) > p2:
            res.append(word1[p1])
            res.append(word2[p2])
            p1+=1
            p2+=1
        if p1 != len(word1):
            res.append(word1[p1:])
        if p2 != len(word2):
            res.append(word2[p2:])
        return "".join(res)