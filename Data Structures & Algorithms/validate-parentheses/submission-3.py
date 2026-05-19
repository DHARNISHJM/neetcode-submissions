class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(", "]": "[", "}": "{"}
        o = list(match.values())
        c = list(match.keys())
        for i in s:
            if i in o:
                stack.append(i)
            elif i.isalnum():
                pass
            elif i in c:
                if len(stack) == 0:
                    return False
                top = stack[len(stack)-1]
                if match[i] == top:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        