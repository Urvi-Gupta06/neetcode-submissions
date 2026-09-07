class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        l = 0
        best = ""
        best_len = float("inf")

        for r in range(len(s)):
            char = s[r]

            if char in need:
                window[char] = window.get(char, 0) + 1

            # Move l while the left character is unnecessary
            while l <= r:
                
                # character isn't needed at all
                if s[l] not in need:
                    l += 1

                # we have extra copies of this character
                elif window[s[l]] > need[s[l]]:
                    window[s[l]] -= 1
                    l += 1

                else:
                    break

            # Check whether current window has everything
            valid = True

            for c in need:
                if window.get(c, 0) < need[c]:
                    valid = False
                    break

            if valid:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best = s[l:r + 1]

        return best