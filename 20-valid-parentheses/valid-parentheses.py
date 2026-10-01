class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # map closing brackets to opening
        pairs = {')': '(', '}': '{', ']': '['}

        # iterate through each char in the string
        for c in s:
            # if it's an opening bracket, push to stack
            if c in pairs.values():
                stack.append(c)
            else:
                # if it's a closing bracket:
                # if stack is empty or top doesn't match expected opening
                if not stack or stack.pop() != pairs.get(c):
                    return False

        # if stack empty at end, all matched
        return len(stack) == 0