class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        l=0
        result=0

        for i in range(len(s)):
            while s[i] in cset:
                cset.remove(s[l])
                l+=1
            cset.add(s[i])
            result = max(result,i-l+1)
        return result