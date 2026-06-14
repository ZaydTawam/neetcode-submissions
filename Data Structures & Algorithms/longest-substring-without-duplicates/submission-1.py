class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, -1
        window = set()

        while r < len(s) - 1:
            r += 1
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])

            longest = max(longest, r - l + 1)
        return longest