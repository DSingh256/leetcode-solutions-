import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=0
        even=0
        
        for i in range(1,n+1):
            odd+=(2*i)+1
            even+=2*i
        return math.gcd(even,odd)