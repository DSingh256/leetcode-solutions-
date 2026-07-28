class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half = "".join(sorted(s[:len(s) // 2]))
        mid = s[len(s) // 2] if len(s) % 2 != 0 else ""
        return half + mid + half[::-1]