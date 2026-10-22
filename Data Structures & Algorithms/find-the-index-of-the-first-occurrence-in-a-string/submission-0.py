class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        if not needle or m>n or not haystack:
            return -1
        
        for i in range(n-m+1):
            j=0
            while j<m:
                if haystack[i+j]!=needle[j]:
                    break
                j+=1
            if j==m:
                return i
        return -1