class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
    
        maxx=0
        for i in range(len(s)):
            arr={}
            for j in range(i,len(s)):
                k=s[j]
                
                arr[k]=arr.get(k, 0) + 1
                if max(arr.values(), default=0) <= 2:
                    z=j-i+1
                    maxx=max(z,maxx)
                
        return maxx
                    
        