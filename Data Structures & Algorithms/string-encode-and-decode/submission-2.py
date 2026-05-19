class Solution:

    def encode(self, strs: List[str]) -> str:
        # string = ""
        # for i in strs:
        #     string = string + "🚀" + i
        # return string
        string = ""
        for i in strs:
            string = string + str(len(i))+ "#" + i
        return string
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            string = s[j+1: j+1+length]
            res.append(string)
            i = j+1+length
        return res