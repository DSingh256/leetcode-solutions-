class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        max_num = max(nums)
        
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1
        
        for num in nums:
            new_dp = [row[:] for row in dp]
            for g1 in range(max_num + 1):
                for g2 in range(max_num + 1):
                    if dp[g1][g2] == 0:
                        continue
                    
                    next_g1 = math.gcd(g1, num) if g1 > 0 else num
                    new_dp[next_g1][g2] = (new_dp[next_g1][g2] + dp[g1][g2]) % MOD
                    
                    next_g2 = math.gcd(g2, num) if g2 > 0 else num
                    new_dp[g1][next_g2] = (new_dp[g1][next_g2] + dp[g1][g2]) % MOD
            dp = new_dp
            
        ans = 0
        for g in range(1, max_num + 1):
            ans = (ans + dp[g][g]) % MOD
            
        return ans