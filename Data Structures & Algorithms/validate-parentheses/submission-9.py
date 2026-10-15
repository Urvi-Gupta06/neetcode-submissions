class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paran = {")": "(", "}":"{", "]":"["}

        for i in s:
            if i in paran:
                if stack and stack[-1]==paran[i]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        return True if not stack else False 

                