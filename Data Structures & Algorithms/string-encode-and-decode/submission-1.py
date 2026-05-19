class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + "🚀" + i
        return string
        

    def decode(self, s: str) -> List[str]:
        list = s.split("🚀")
        list.pop(0)
        return list