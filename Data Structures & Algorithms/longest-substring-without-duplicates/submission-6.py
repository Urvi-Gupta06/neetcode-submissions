class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        helper = set()

        for r in range(len(s)):
            while s[r] in helper:
                helper.remove(s[l])
                l+=1
            helper.add(s[r])
            res = max(res,r-l+1)
        return res
