class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                if len(stack) >= 2:
                    r = stack.pop()
                    l = stack.pop()
                    match i:
                        case "+":
                            stack.append(l+r)
                        case "*": 
                            stack.append(l*r)
                        case "-":
                            stack.append(l-r)                        
                        case "/":
                            stack.append(int(l/r))
            else:
                stack.append(int(i))
        return stack[-1]

