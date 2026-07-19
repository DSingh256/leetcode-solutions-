class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last={c:i for i,c in enumerate(s)}
        stack=[]
        visited=set()
        for i, char in enumerate(s):
            if char not in visited:
                while stack and char<stack[-1]and i< last[stack[-1]]:
                    remove=stack.pop()
                    visited.remove(remove)
                stack.append(char)
                visited.add(char)    
        return "".join(stack)    