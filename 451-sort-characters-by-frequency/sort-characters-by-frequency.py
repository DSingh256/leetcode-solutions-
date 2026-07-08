from collections import Counter
class Solution:
    def frequencySort(self,s: str):
        counts = Counter(s)
        chars = sorted(counts.keys(), key=lambda c: (-counts[c], c))
        return ''.join(c * counts[c] for c in chars)    