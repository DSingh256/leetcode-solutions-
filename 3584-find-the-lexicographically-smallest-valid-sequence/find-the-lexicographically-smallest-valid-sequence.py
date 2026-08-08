class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        last = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        ans = []
        i = 0
        changed = False

        for j in range(m):
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    found = True
                    break
                elif not changed:
                    if j == m - 1 or last[j + 1] > i:
                        ans.append(i)
                        i += 1
                        changed = True
                        found = True
                        break
                i += 1
            if not found:
                return []

        return ans