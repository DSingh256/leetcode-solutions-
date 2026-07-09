class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        j = 0
        while j < n and s[j] == " ":
            j += 1

        sign = 1
        if j < n and s[j] == '+':
            sign = 1
            j += 1
        elif j < n and s[j] == '-':
            sign = -1
            j += 1

        ans = []
        while j < n and s[j].isdigit():
            ans.append(s[j])
            j += 1

        if not ans:
            return 0

        num = int("".join(ans)) * sign

        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        return num