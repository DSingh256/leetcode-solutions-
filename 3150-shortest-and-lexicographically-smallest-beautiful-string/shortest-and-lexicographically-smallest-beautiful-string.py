class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if '1' not in s:
            return ""
        i=0
        ans = ""
        count = 0
        for j in range(len(s)):
            if s[j] == '1':
                count += 1

            while count == k:
                sub = s[i : j + 1]

                if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                    ans = sub

                if s[i] == '1':
                    count -= 1
                i += 1

        return ans