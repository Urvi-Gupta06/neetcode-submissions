class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string+=i
        lower = string.lower()
        reverse = lower[::-1]
        return lower == reverse

