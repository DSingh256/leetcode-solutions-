from typing import List

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        if self.n == 0:
            return
        self.K = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.K)]
        self.st[0] = list(arr)
        for j in range(1, self.K):
            length = 1 << j
            half = 1 << (j - 1)
            for i in range(self.n - length + 1):
                self.st[j][i] = max(self.st[j - 1][i], self.st[j - 1][i + half])

    def query(self, L, R):
        if L > R or L < 0 or R >= self.n or self.n == 0:
            return 0
        j = (R - L + 1).bit_length() - 1
        return max(self.st[j][L], self.st[j][R - (1 << j) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        seg_char = []
        seg_start = []
        seg_end = []
        seg_len = []
        seg_id = [0] * n
        
        start = 0
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                length = i - start + 1
                idx = len(seg_char)
                seg_char.append(s[i])
                seg_start.append(start)
                seg_end.append(i)
                seg_len.append(length)
                for k in range(start, i + 1):
                    seg_id[k] = idx
                start = i + 1
                
        m = len(seg_char)
        
        gain = [0] * m
        for i in range(m):
            if seg_char[i] == '1':
                if i - 1 >= 0 and i + 1 < m:
                    gain[i] = seg_len[i - 1] + seg_len[i + 1]
                    
        st = SparseTable(gain)
        
        ans = []
        for l, r in queries:
            l_seg = seg_id[l]
            r_seg = seg_id[r]
            
            max_gain = 0
            
            if l_seg + 2 <= r_seg - 2:
                max_gain = max(max_gain, st.query(l_seg + 2, r_seg - 2))
                
            candidates = {l_seg, l_seg + 1, l_seg + 2, r_seg - 2, r_seg - 1, r_seg}
            for i in candidates:
                if 0 <= i < m and seg_char[i] == '1':
                    if seg_start[i] >= l and seg_end[i] <= r:
                        left_zeros = 0
                        right_zeros = 0
                        
                        if seg_start[i] > l:
                            prev_start = seg_start[i - 1] if i - 1 >= 0 else -1
                            left_zeros = seg_start[i] - max(prev_start, l)
                            
                        if seg_end[i] < r:
                            next_end = seg_end[i + 1] if i + 1 < m else n
                            right_zeros = min(next_end, r) - seg_end[i]
                            
                        if left_zeros > 0 and right_zeros > 0:
                            max_gain = max(max_gain, left_zeros + right_zeros)
                            
            ans.append(total_ones + max_gain)
            
        return ans